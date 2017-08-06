import os
from flask import Flask, render_template, json, send_from_directory, jsonify
from rq import Queue
from rq.job import Job
from worker import conn
from scraper import Scraper

app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, 'static', 'data.json')
q = Queue(connection=conn)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(directory='static', filename='favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET', 'POST'])
def main():
    json_data = open(json_url, 'r')
    data = json.load(json_data)
    return render_template('index.html', news=data[:20])


@app.route('/scrape', methods=['POST'])
def scrape():
    scraper = Scraper()
    job = q.enqueue_call(
        func=scraper.scrape, args=(json_url,), result_ttl=5000, timeout=10000
    )
    return job.get_id()


@app.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):
    job = Job.fetch(job_key, connection=conn)
    if job.is_finished:
        return jsonify(job.result)
    else:
        return "Scraping...", 202


@app.route('/get-json', methods=['GET'])
def get_json():
    scraper = Scraper()
    return jsonify(scraper.return_json(json_url))


@app.route('/download')
def download():
    return send_from_directory(directory='static', filename='data.json', as_attachment=True)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

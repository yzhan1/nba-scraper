import os
from flask import Flask, render_template, json, send_from_directory, request, redirect, url_for

from scraper import Scraper

app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, 'static', "data.json")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        json_data = open(json_url, 'r')
        data = json.load(json_data)
        return render_template('main.html', news=data[:20])
    elif request.method == 'POST':
        scraper = Scraper()
        new_data = scraper.scrape()
        return render_template('scrape.html', news=new_data[:20])


#
# @app.route('/scraping', methods=['POST'])
# def scrape():
#


@app.route('/download')
def get_json():
    return send_from_directory(directory='static', filename='data.json', as_attachment=True)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

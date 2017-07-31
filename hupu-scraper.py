import os
from flask import Flask, render_template, json, send_from_directory

from scraper import Scraper

app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, 'static', "data.json")
json_data = open(json_url, 'r')
data = json.load(json_data)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/')
def main():
    scraper = Scraper()
    return render_template('main.html', news=data)


@app.route("/download")
def getJSON():
    return send_from_directory(directory='static', filename='data.json', as_attachment=True)


if __name__ == '__main__':
    app.run()

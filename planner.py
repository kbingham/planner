#!/usr/bin/python3

from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


# https://markhneedham.com/blog/2017/04/27/python-flask-generating-a-static-html-page/
if __name__ == "__main__":
    with app.app_context():
        rendered = render_template('year.html', \
            title = "2019", \
            people = [{"name": "Mark"},
                      {"name": "Michael"}])
        print(rendered)


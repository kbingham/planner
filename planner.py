#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/2019')
def year():
    current = 2019
    with app.app_context():
        return render_template('year.html', \
            title = "2019 Year Planner", \
            weekdays = [ 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' ],
            months = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ],
        )


@app.route('/')
def index():
    return year()


# https://markhneedham.com/blog/2017/04/27/python-flask-generating-a-static-html-page/
if __name__ == "__main__":
    app.config['SERVER_NAME'] = "localhost"
    with app.app_context():
        print(year())

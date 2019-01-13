#!/usr/bin/python3

import calendar
from flask import Flask, render_template

app = Flask(__name__)
cal = calendar.Calendar()

# itermonthdays generates data after the last date in the month.
# Prevent this by converting the generator to a list, and splicing it.
def month_dates(year, month):
    for d in list(cal.itermonthdays(year, month))[:37]:
        yield d if d else ''


def month_dates2(year, month):
    m = calendar.monthcalendar(year, month)
    for w in m:
        for d in w:
            yield d if d else ''


@app.route('/2019')
def year():
    current = 2019
    with app.app_context():
        return render_template('year.html', \
            title = "2019 Year Planner", \
            weekdays = calendar.day_abbr,
            months = calendar.month_abbr,
            dates = month_dates,
        )


@app.route('/')
def index():
    return year()


# https://markhneedham.com/blog/2017/04/27/python-flask-generating-a-static-html-page/
if __name__ == "__main__":
    app.config['SERVER_NAME'] = "localhost"
    with app.app_context():
        print(year())

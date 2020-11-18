

from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


class ParseEvents:

    def __init__(self):
        self.url = 'https://www.python.org/events/python-events/'
        self.html = self.get_html()
        self.base_url = 'https://www.python.org'

    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False

    def get_events(self):
        soup = BeautifulSoup(self.html, 'html.parser'). \
            find('ul', class_='list-recent-events menu').find_all('li')
        all_events = []
        for tag in soup:
            a = tag.find('h3').find('a')
            title = a.string
            path = self.base_url + a.get('href')
            datestring = tag.find('time').get('datetime')
            date = dt.strptime(datestring, "%Y-%m-%dT%H:%M:%S+00:00")
            event = {'title': title,
                     'path': path,
                     'dt': date.date()}
            if date.month in [11, 12]:
                all_events.append(event)
        return all_events


@app.route('/')
def event():
    parser = ParseEvents()
    events = parser.get_events()
    return render_template('index.html',
                           title='События Python.org (ноябрь, декабрь)',
                           events=events)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

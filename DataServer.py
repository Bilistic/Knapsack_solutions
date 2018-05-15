from flask import Flask, render_template, send_from_directory
import pandas as pd
import json
import os

app = Flask(__name__)


class GraphData:

    def __init__(self):
        self.count = 0
        self.total = 0
        self.average = 0

    def get_average(self):
        self.average = self.total / self.count
        return self.average

    def add(self, amount):
        self.count += 1
        self.total += amount


@app.route('/get_data/')
def get_data():
    df = pd.read_excel('Results.xlsx')
    return df.to_json(orient='index')


@app.route('/get_data/<string:name>/')
def get_data_spec(name):
    df = pd.read_excel('Results.xlsx')
    df = df[[name, 'Node Amount']]
    df = df.dropna().values.tolist()
    y = dict()
    for x in df:
        if isinstance(x[0], float) is True:
            xy = y.get(x[1], GraphData())
            xy.add(x[0])
            y[x[1]] = xy
    df = json.dumps([{"y": value.get_average(), "x": int(key)} for key, value in y.items()])
    return df


@app.route('/favicon.ico/')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)


if __name__ == '__main__':
    app.run()

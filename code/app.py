import time
import os
import redis
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for


app = Flask(__name__)
cache = redis.Redis(host=os.environ['ENDPOINT'], port=os.environ['PORT'], decode_responses=True)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
def get_names():
    retries = 5
    while True:
        try:
            return cache.lrange('names', 0, -1)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
def push_name(name):
    retries = 5
    while True:
        try:
            return cache.lpush('names', name)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
def delete_names():
    retries = 5
    while True:
        try:
            return cache.delete('names')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    names_list = get_names()
    return render_template('index.html', times = count, server = "Server", names= names_list)

@app.route('/newname')
def newname():
    name = request.args.get("name")
    push_name(name)
    return name

@app.route('/delete')
def delete():
    delete_names()
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
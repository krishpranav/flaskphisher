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

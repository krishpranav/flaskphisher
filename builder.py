#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

# imports
import sys
import os
import shutil
import urllib2

from bs4 import BeautifulSoup

# relative root url
def relative_root(url):
    if '?' in url:
        url = url[:url.find('?')]
    if url.count('/') == 2:
        return url + '/'
    else:
        return url[:url.rfind('/')] + '/'

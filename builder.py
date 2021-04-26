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


# absolute root
def absolute_root(url):
    if '?' in url:
        url = url[:url.find('?')]
    if url.count('/') == 2:
        return url
    else:
        return url[:url.find('/',8)]

# relatvie to absolute
def relative_to_absolute(url, link):
    if link.startswith('http://') or link.startswith('https://') or link.startswith('data:'):
        # already absolute, skipping
        return link
    if link.startswith('//'):
        # just add protocol
        link = 'http:' + link
        return link
    if link[0] == '/':
        # Absolute URL
        link = absolute_root(url) + link
        return link
    else:
        # Relative URL
        link = relative_root(url) + link
        return link

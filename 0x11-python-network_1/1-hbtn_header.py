#!/usr/bin/python3
"""
A script that gets the value of an header
"""
import urllib.request
import sys
import socket

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))

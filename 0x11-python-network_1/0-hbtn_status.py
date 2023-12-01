#!/usr/bin/python3
"""
A script that fetches a url and prints the body
"""
import urllib.request

response = urllib.request.urlopen("https://alx-intranet.hbtn.io/status")
data = response.read()
print("Body response:")
print(f'\t- type: {type(data)}')
print(f'\t- content: {data}')
print(f'\t- utf8 content: {data.decode("utf-8")}')

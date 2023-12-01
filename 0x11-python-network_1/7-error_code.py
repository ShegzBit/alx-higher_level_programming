#!/usr/bin/python3
"""
Python script that takes in a URL, sends a
request to the URL and displays the body of the
response
"""
import sys
import requests as req

if __name__ == "__main__":
    url = sys.argv[1]
    res = req.get(url)
    try:
        res.raise_for_status()
        print(res.text)
    except req.exceptions.HTTPError as e:
        print(f"Error code: {res.status_code}")

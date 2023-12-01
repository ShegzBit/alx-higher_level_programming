#!/usr/bin/python3
"""
Python script that takes in a letter and sends
a POST request to
"""
import requests as req
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    res = req.post(url, data={"q": q})
    try:
        result = res.json()
        if 'id' in result and 'name' in result:
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")

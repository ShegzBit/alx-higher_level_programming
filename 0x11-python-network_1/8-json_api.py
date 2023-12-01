#!/usr/bin/python3
"""
Python script that takes in a letter and sends
a POST request to
"""
import requests as req
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    search = sys.argv[1] if len(sys.argv) > 2 else ""
    payload = {"q": search}
    res = req.post(url, data=payload)
    try:
        my_dict = res.json()
    except req.json.JSONDecodeError as e:
        print("Not a valid JSON")
        exit(0)
    if not my_dict:
        print("No result")
        exit(0)
    print(f"[{my_dict.get('id')}] my_dict.get('name')")

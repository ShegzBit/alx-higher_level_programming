#!/usr/bin/python3
"""
Write a Python script that fetches
https://alx-intranet.hbtn.io/status
"""

import requests as req
url = "https://alx-intranet.hbtn.io/status"

res = req.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print(f"\t- type: {type(res.text)}")
print(f"\t- content: {res.text}")

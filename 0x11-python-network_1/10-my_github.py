#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id
"""
import sys
import requests as req

if __name__ == "__main__":
    user, passwd = sys.argv[1:]
    header = {"Accept": "application/vnd.github+json",
              "Authorization": f"Bearer {passwd}",
              "X-GitHub-Api-Version": "2022-11-28"}
    url = f"https://api.github.com/users/{user}"

    res = req.get(url, headers=header)
    json = res.json()
    print(json.get('id'))

#!/usr/bin/python3
"""
A script that lists 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails” You must use the GitHub API,
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests as req
import sys

if __name__ == "__main__":
    repo, user = sys.argv[1:]

    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    url = f"https://api.github.com/repos/{user}/{repo}/commits"

    with open('store.json', 'w', encoding='utf-8') as f:
        import json
        res = req.get(url, headers=headers)
        commit_list = res.json()[:10]
        for commit in commit_list:
            print(f"{commit.get('sha')}: \
{commit.get('commit').get('author').get('name')}")

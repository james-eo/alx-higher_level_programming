#!/usr/bin/python3
""" Lists the recent 10 commits in a Github repository and the committer
"""
import requests
import sys


if __name__ == "__main__":
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    request = requests.get(url)

    commits = request.json()
    for commit in commits[:10]:
        sha = commit.get("sha")
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {committer}")

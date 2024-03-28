#!/usr/bin/python3
""" Lists the recent 10 commits in a Github repository and the committer
"""
import requests
import sys


def list_commits(repository, owner):
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository> <owner>")
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]

    list_commits(repository, owner)

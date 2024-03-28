#!/usr/bin/python3
"""Fetches a URL and displays the body of the response"""

from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

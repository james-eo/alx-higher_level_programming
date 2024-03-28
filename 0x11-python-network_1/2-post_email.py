#!/usr/bin/python3
"""Sends a POST request with email parameter to the specified URL,
and displays the body of the response
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    content = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, content)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

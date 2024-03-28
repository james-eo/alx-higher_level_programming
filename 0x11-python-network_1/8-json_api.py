#!/usr/bin/python3
"""Sends a POST request with a letter as a parameter"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    data = {'q': letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json_resp = response.json()

        if json_resp:
            print("[{}] {}".format(json_resp['id'], json_resp['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

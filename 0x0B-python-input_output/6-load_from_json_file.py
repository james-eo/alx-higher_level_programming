#!/usr/bin/python3

"""Creates an object from JSON"""
import json


def load_from_json_file(filename):

    """ a function that creates an Object from a “JSON file”
    Arguments:
    @filename: the file to write into
    Returns: an objest"""

    with open(filename, 'r') as f:
        return json.loads(f.read())

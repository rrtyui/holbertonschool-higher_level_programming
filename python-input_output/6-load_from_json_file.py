#!/usr/bin/python3
"""creates an object from JSON”"""


import json


def load_from_json_file(filename):
    """create a JSON file"""
    with open(filename, 'r') as out_file:
        return json.load(out_file)

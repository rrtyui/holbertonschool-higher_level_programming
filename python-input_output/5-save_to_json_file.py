#!/usr/bin/python3
"""object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """save object to a file"""
    with open(filename, 'w+') as file_open:
        file_open.write(json.dumps(my_obj))

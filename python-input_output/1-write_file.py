#!/usr/bin/python3
"""function that writes into a text file"""


def write_file(filename="", text=""):
    """return number of characters written"""
    with open(filename, 'w') as file_read:
        return file_read.write(text)

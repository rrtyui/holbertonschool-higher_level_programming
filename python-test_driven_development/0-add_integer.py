#!/usr/bin/python3
"""add integr"""


def add_integer(a, b=98):
    """sums the to numbers added to the function"""
    if (a is None or not isinstance(a, int) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

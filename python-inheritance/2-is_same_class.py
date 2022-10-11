#!/usr/bin/python3
"""function checks if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """returns  if the object is exactly an instance"""
    return issubclass(a_class, type(obj))

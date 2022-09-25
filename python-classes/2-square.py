#!/usr/bin/python3
"""Squareclass"""


class Square:
    """Class that defines a square """
    def __init__(self, size=0):
        """Init class"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

#!/usr/bin/python3
"""a class rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class rectangle """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        self.m_area = height * width

    def area(self):
        super().__init__()
        return self.m_area

    def __str__(self):
        super().__init__()
        module = f"[Rectangle] {self.__width}/{self.__height}"
        return (module)

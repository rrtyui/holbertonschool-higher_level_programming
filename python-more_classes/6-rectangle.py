#!/usr/bin/python3
"""class"""


class Rectangle():
    """Class Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        st = ''
        if self.__height == 0 or self.__width == 0:
            st = ''
        else:
            for i in range(self.__height):
                st += '#' * self.__width
                if i != self.__height - 1:
                    st += '\n'
        return (st)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

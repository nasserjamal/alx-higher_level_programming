#!/usr/bin/python3
"""
Looks like this module has an even more advanced defination of the
 class rectangle
"""


class Rectangle:
    """Represents a rectangle. Yeah I know!!! Very basic defination :|"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        res = ""
        if 0 in (self.__height, self.__width):
            return res
        for height in range(0, self.__height):
            for width in range(0, self.__width):
                res += '#'
            if height != self.__height - 1:
                res += '\n'
        return res

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if 0 not in (self.__height, self.__width):
            return 2 * (self.__height + self.__width)
        else:
            return 0

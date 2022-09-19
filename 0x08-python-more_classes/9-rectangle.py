#!/usr/bin/python3
"""
Looks like this module has an even more more advanced defination
 of the class rectangle
"""


class Rectangle:
    """Represents a rectangle. Yeah I know!!! Very basic defination :|"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        res = ""
        if 0 in (self.__height, self.__width):
            return res
        for height in range(0, self.__height):
            for width in range(0, self.__width):
                res += str(self.print_symbol)
            if height != self.__height - 1:
                res += '\n'
        return res

    def __repr__(self):
        return self.__class__.__name__ + "(" + str(self.__width)\
         + ", " + str(self.__height) + ")"

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if(type(rect_1) is not Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if(type(rect_2) is not Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if(rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

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

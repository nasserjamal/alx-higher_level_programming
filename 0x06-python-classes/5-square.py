#!/usr/bin/python3
"""Module description goes here"""


class Square:
    """Defines what a square is????!!!"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for row in range(0, self.__size):
                for column in range(0, self.__size):
                    print("#", end="")
                print("")

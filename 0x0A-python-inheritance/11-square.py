#!/usr/bin/python3
"""This module contains defination for Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class containing the defination of a square"""

    def __init__(self, size):
        self.__size = super().integer_validator("size", size)

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

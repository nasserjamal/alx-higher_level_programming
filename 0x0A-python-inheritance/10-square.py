#!/usr/bin/python3
"""This module contains defination for Square class"""
from curses.textpad import rectangle


Rectangle = __import__("9-rectangle").BaseGeometry


class Square(Rectangle):
    """Class containing the defination of a square"""

    def __init__(self, size):
        self.__size = super().integer_validator("size", size)

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

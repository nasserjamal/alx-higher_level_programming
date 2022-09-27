#!/usr/bin/python3
"""This module contains defination for Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class containing the defination of a rectangle"""

    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        return (self.__height * self.__width)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

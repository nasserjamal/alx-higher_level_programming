#!/usr/bin/python3
"""The base module: Contains the base class"""


class Base:
    """This class is the base for all other classes.
    It's function is to manage id attribute of all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__class__.__nb_objects

#!/usr/bin/python3
"""My list module"""


def inherits_from(obj, a_class):
    """Checks if the object is a subclass of the class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class

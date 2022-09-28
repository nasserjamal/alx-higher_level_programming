#!/usr/bin/python3
"""Module containing the student class"""


class Student:
    """Classdefining theproperties of a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts class to json"""
        return self.__dict__

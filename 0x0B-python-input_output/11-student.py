#!/usr/bin/python3
"""Module containing the student class"""


class Student:
    """Class defining the properties of a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts class to json"""
        if type(attrs) == list:
            result = {}
            for item in attrs:
                if item in self.__dict__:
                    result[item] = self.__dict__[item]
            return result
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Convert json to class attributes"""
        for item in json:
            if item in self.__dict__:
                self.__dict__[item] = json[item]

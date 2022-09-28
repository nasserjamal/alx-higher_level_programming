#!/usr/bin/python3
"""Returns dictionary description"""


def class_to_json(obj):
    """Converts class to json"""
    return obj.__dict__

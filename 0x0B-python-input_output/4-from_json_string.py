#!/usr/bin/python3
"""Writing json files"""


import json


def from_json_string(my_str):
    """Converts json string to python object"""
    return json.loads(my_str)

#!/usr/bin/python3
"""Writing json files"""


import json


def to_json_string(my_obj):
    """Returns json representation of my_obj"""
    return json.dumps(my_obj)

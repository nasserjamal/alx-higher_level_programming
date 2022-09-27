#!/usr/bin/python3
"""Writing json files"""


import json


def save_to_json_file(my_obj, filename):
    """Saves a string to file as json formart"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
"""Module for loading data from json files"""


import json


def load_from_json_file(filename):
    """Loads data from json files"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

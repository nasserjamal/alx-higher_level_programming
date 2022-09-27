#!/usr/bin/python3
"""Module for loading data from json files"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
try:
    lst = load_from_json_file("add_item.json")
except FileNotFoundError:
    lst = []
lst.extend(sys.argv[1:])
save_to_json_file(lst, "add_item.json")

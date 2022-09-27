#!/usr/bin/python3
"""Module for appending to a file"""


def append_write(filename="", text=""):
    """Appends text into a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

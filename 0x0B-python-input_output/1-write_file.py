#!/usr/bin/python3
"""Module for writing a file"""


def write_file(filename="", text=""):
    """Writes a string into a  file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

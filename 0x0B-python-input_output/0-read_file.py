#!/usr/bin/python3
"""Module for reading a file"""


def read_file(filename=""):
    """Reads and outputs the file content to the stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
        print(data, end="")

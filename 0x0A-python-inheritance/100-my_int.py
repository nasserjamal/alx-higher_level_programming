#!/usr/bin/python3
"""Module containing my int class"""


class MyInt(int):
    """My int class that inheritsfrom int"""
    def __eq__(self, __x: object):
        return not super().__eq__(__x)

    def __ne__(self, __x: object):
        return not super().__ne__(__x)

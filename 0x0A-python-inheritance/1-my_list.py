#!/usr/bin/python3
"""My list module"""


class MyList(list):
    """A new and improved type of list class"""

    def print_sorted(self):
        """Prints the list in a sorted way"""
        print(sorted(self))
        return(sorted(self))

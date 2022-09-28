#!/usr/bin/python3
"""Module Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of integers representing the pascals triangle of n"""
    rslt = []
    for row in range(0, n):
        rslt.append([])
        for cln in range(0, row+1):
            if(cln == 0 or cln == row):
                rslt[row].append(1)
            else:
                rslt[row].append(rslt[row - 1][cln - 1] + rslt[row - 1][cln])
    return rslt

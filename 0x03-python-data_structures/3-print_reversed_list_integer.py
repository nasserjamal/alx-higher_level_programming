#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    newList = my_list.copy()
    newList.reverse()
    for int in newList:
        print("{:d}".format(int))

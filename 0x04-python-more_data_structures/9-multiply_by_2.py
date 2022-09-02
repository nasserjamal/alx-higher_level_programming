#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_new_dictionary = {}
    for key, value in a_dictionary.items():
        new_value = value * 2
        a_new_dictionary[key] = new_value
    return a_new_dictionary

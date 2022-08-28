#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for letter in my_string:
        if letter != "c" and letter != "C":
            newString += letter
    return newString

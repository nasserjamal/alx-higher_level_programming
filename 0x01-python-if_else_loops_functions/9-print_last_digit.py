#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last = number % 10
    else:
        last = 10 - (number % 10)
    print(last, end="")
    return last

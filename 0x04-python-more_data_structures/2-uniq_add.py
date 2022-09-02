#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    unique_list = list(my_set)
    sum = 0

    for num in unique_list:
        sum += num
    return sum

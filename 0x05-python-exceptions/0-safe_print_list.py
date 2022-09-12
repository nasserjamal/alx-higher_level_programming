#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    tempNum = 0
    for num in my_list[:x]:
        try:
            print("{:d}".format(num), end="")
        except ValueError:
            print("{}".format(num), end="")
        tempNum += 1
    print("".format())
    return (tempNum)

#!/usr/bin/python3
number = range(0, 99)
for num in number:
    i = (int)(num / 10)
    j = (int)(num % 10)
    if j > i and num != 89:
        print("{:02d}".format(num), end=', ')
    elif num == 89:
        print("{:02d}".format(num))

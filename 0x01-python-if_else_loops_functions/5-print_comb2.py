#!/usr/bin/python3
number = range(0, 100)
for i in number:
    if i != 99:
        print("{:02d}".format(i), end=', ')
    else:
        print("{:02d}".format(i))

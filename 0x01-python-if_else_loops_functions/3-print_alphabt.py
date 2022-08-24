#!/usr/bin/python3
numbers = range(97, 123)
for i in numbers:
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end='')

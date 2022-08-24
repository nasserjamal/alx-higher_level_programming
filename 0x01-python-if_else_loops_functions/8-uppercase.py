#!/usr/bin/python3
def uppercase(c):
    value = ""
    for i in list(c):
        if ord(i) >= 97 and ord(i) <= 122:
          value += chr((ord(i) - 97) + ord('A'))
        else:
            value += i
    else:
        print(value)

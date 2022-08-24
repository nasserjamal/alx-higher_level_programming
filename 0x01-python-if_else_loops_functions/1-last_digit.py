#!/usr/bin/python3
import math
import random
number = random.randint(-10000, 10000)
lastDigit = math.fmod(number, 10)
string = f"Last digit of {number} is {lastDigit}"
if lastDigit > 5:
    print(string, "and is greater than 5")
elif lastDigit == 0:
    print(string, "and is 0")
elif lastDigit < 6:
    print(string, "and is less than 6 and not 0")

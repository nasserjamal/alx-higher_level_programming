#!/usr/bin/python3
"""Module description goes here"""


class Square:
    """Defines what a square is????!!!"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) == tuple and len(value) == 2:
            if all(type(i) == int and i >= 0 for i in value):
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive \
integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for posy in range(0, self.__position[1]):
                print("")
            for row in range(0, self.__size):
                for posx in range(0, self.__position[0]):
                    print(" ", end="")
                for column in range(0, self.__size):
                    print("#", end="")
                print("")

    def __str__(self):
        ans = ""
        if self.__size == 0:
            ans = "\n"
        else:
            for posy in range(0, self.__position[1]):
                ans += "\n"
            for row in range(0, self.__size):
                for posx in range(0, self.__position[0]):
                    ans += " "
                for column in range(0, self.__size):
                    ans += "#"
                ans += "\n"
        if len(ans) >= 1:
            ans = ans[:-1]
        return ans

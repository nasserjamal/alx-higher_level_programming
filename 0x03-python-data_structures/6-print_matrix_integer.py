#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for noList in matrix:
        for i in range(len(noList)):
            if i == len(noList) - 1:
                print("{:d}".format(noList[i]))
            else:
                print("{:d} ".format(noList[i]), end="")

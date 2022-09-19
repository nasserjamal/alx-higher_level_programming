#!/usr/bin/python3
"""The nqueens soultion mdule"""


import sys


class nQueens:
    """Analysses the nqueens problem using backtracking"""

    def __init__(self, N):
        self.n = N
        self.solutions = []
        self.backtrack(SlnSet(), 0)
        self.printSolutions()

    def printSolutions(self):
        for sln in self.solutions:
            print(sln)

    def backtrack(self, slnSet, r):
        if r == self.n:
            self.solutions.append([pos for pos in slnSet.ansSheet])
            return

        for c in range(0, self.n):
            if slnSet.isQpositionValid(r, c):
                slnSet.addValues(r, c)
                self.backtrack(slnSet, r + 1)
                slnSet.popValues()


class SlnSet:
    """A set of possible solutions"""

    def __init__(self):
        self.ansSheet = []
        self.r = []  # Invalid rows
        self.c = []  # Invalid columns
        self.pd = []  # Invalid positive diagnols
        self.nd = []  # Invalid negative diagnols

    def isQpositionValid(self, r, c):
        if r in self.r or c in self.c or r + c in self.pd or r - c in self.nd:
            return False
        else:
            return True

    def addValues(self, r, c):
        self.r.append(r)
        self.c.append(c)
        self.pd.append(r + c)
        self.nd.append(r - c)
        self.ansSheet.append([r, c])

    def popValues(self):
        self.r.pop()
        self.c.pop()
        self.pd.pop()
        self.nd.pop()
        self.ansSheet.pop()


if (len(sys.argv) != 2):
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)
nQueens(N)

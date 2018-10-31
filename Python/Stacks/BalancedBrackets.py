#!/bin/python3

import math
import os
import random
import re
import sys


def printIsBalanced(brackets):
    result = isBalanced(brackets)
    if result:
        print("YES")
    else:
        print("NO")


def isBalanced(brackets):
    openingBrackets = ["(", "[", "{"]
    closingBrackets = [")", "]", "}"]
    bracketsDict = {}
    stack = []

    for bracketType in range(len(openingBrackets)):
        bracketsDict[openingBrackets[bracketType]] = closingBrackets[bracketType]

    for bracket in brackets:
        if bracket in openingBrackets:
            stack.append(bracket)
        elif bracket in closingBrackets:
            if not stack or bracketsDict[stack.pop()] != bracket:
                return False
        else:
            return False

    if stack:
        return False
    return True


if __name__ == '__main__':
    sys.stdin = open("BalancedBrackets_input.txt")

    t = int(input())

    for _ in range(t):
        s = input()

        printIsBalanced(s)


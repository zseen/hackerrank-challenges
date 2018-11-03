#!/bin/python3

import math
import os
import random
import re
import sys


BRACKETS_DICT = {"(": ")", "[": "]", "{": "}"}

def printIsBalanced(brackets):
    result = isBalanced(brackets)
    if result:
        print("YES")
    else:
        print("NO")


def isBalanced(brackets):
    stack = []

    for bracket in brackets:
        if bracket in BRACKETS_DICT.keys():
            stack.append(bracket)
        else:
            if not stack or bracket != BRACKETS_DICT[stack.pop()]:
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


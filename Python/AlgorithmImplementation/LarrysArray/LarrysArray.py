#!/bin/python3

import math
import os
import random
import re
import sys


def larrysArray(numsArray):
    inversionCounter = 0
    for i in range(0, len(numsArray)):
        for j in range(i + 1, len(numsArray)):
            if numsArray[i] > numsArray[j]:
                inversionCounter += 1

    if inversionCounter % 2 == 0:
        return True

    return False


def main():
    sys.stdin = open("LarrysArray_input.txt")
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)
        print(result)


if __name__ == '__main__':
    main()


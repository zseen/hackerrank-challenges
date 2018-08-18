#!/bin/python3
from collections import *


import sys


def differenceIsLessThanOne(numbersList):
    maximum = 0
    for item in numbersList:
        numBig = numbersList.count(item)
        numSmall = numbersList.count(item - 1)
        total = numBig + numSmall
        if total > maximum:
            maximum = total
    return maximum


def main():
    sys.stdin = open('PickingNumbers_input.txt')
    n = int(input().strip())
    numbersList = [int(a_temp) for a_temp in input().strip().split(' ')]
    maxPairs = differenceIsLessThanOne(numbersList)
    print(maxPairs)


if __name__ == "__main__":
    main()

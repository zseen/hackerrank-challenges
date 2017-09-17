#!/bin/python3
from collections import *


import sys


def differenceIsLessThanOne(numbersList):
    #counter = Counter(numbersList).most_common()
    #print(counter)
    # biggerNum = 0
    # howManyBigger = 0
    # smallerNum = 0
    # howManySmaller = 0
    # middlenum = 0
    # howManyMiddle = 0
    # for item in counter:
    #     middleNum = counter[0][0]
    #     howManyMiddle = counter[0][1]
    #     if item[0] - 1 == middleNum:
    #         biggerNum = item[0]
    #         howManyBigger = item[1]
    #     elif item[0] + 1 == middleNum:
    #         smallerNum = item[0]
    #         howManySmaller = item[1]
    # if howManyBigger > howManySmaller:
    #     return howManyMiddle + howManyBigger
    # return howManySmaller + howManyMiddle

    maximum = 0
    for item in numbersList:
        howManyBig = numbersList.count(item)
        howManySmall = numbersList.count(item - 1)
        howManyBig = howManyBig + howManySmall
        if howManyBig > maximum:
            maximum = howManyBig
    return maximum


def main():
    sys.stdin = open('pickingNumbers_input.txt')
    n = int(input().strip())
    numbersList = [int(a_temp) for a_temp in input().strip().split(' ')]
    maxPairs = differenceIsLessThanOne(numbersList)
    print(maxPairs)


if __name__ == "__main__":
    main()

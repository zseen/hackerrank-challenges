#!/bin/python3


import math
import os
import random
import re
import sys


def maxMin(itemsNumInSubArray, numbersList):
    sortedArr = sorted(numbersList)
    firstSubArray = sortedArr[0: itemsNumInSubArray]
    lowestNum = firstSubArray[0]
    highestNum = firstSubArray[itemsNumInSubArray - 1]
    lowestDifferenceBetweenMaxMin = highestNum - lowestNum

    for i in range(0, len(sortedArr) - itemsNumInSubArray + 1):
        subArray = sortedArr[i: i + itemsNumInSubArray]
        lowestNum = subArray[0]
        highestNum = subArray[itemsNumInSubArray - 1]
        differenceBetweenMaxMin = highestNum - lowestNum
        if differenceBetweenMaxMin < lowestDifferenceBetweenMaxMin:
            lowestDifferenceBetweenMaxMin = differenceBetweenMaxMin

    return lowestDifferenceBetweenMaxMin


if __name__ == '__main__':
    sys.stdin = open("MaxMinInput.txt")

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(result)


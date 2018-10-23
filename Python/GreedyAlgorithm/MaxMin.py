#!/bin/python3
from Library.Sorting import CountingSort

import math
import os
import random
import re
import sys


def maxMin(itemsNumInSubArray, numbersList):
    sortedArr = CountingSort.sortListOfNumbers(numbersList)
    firstSubArray = sortedArr[0:itemsNumInSubArray]
    lowestNum = min(firstSubArray)
    highestNum = max(firstSubArray)
    lowestDifferenceBetweenMaxMin = highestNum - lowestNum

    for i in range(0, len(sortedArr) - itemsNumInSubArray + 1):
        subArray = sortedArr[i:i + itemsNumInSubArray]
        #print(subArray)
        lowestNum = min(subArray)
        highestNum = max(subArray)
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


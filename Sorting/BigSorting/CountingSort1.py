#!/bin/python3

from collections import *

import sys


def countingSort(listOfNumbers):
    cnt = Counter(listOfNumbers)
    cntValueList = []

    for i in range(0,100):
        cntValueList.append(cnt[i])

    return cntValueList


def main():
    sys.stdin = open('CountingSort1_input.txt')
    n = int(input().strip())
    listOfNumbers = list(map(int, input().strip().split(' ')))
    result = countingSort(listOfNumbers)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()


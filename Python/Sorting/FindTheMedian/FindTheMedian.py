#!/bin/python3

import sys
from Library.Sorting import CountingSort


def findMedian(numbersList):
    sortedListOfNumbers = CountingSort.sortListOfNumbers(numbersList)
    median = sortedListOfNumbers[len(sortedListOfNumbers) // 2]

    return median


def main():
    sys.stdin = open('FindTheMedian_input.txt')
    n = int(input().strip())
    numbersList = list(map(int, input().strip().split(' ')))
    result = findMedian(numbersList)
    print(result)

if __name__ == "__main__":
    main()

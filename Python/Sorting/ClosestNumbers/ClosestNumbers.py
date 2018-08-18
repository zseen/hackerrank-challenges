#!/bin/python3

import sys
from Library.Sorting import CountingSort


def closestNumbers(listOfNumbers):
    sortedNumList = CountingSort.sortListOfNumbers(listOfNumbers)

    minDiff = sys.maxsize

    for index in range(1, len(sortedNumList)):
        minDiff = min(minDiff, sortedNumList[index] - sortedNumList[index - 1])

    lowestDifferenceNumbersList = []

    for index in range(1, len(sortedNumList)):
        biggerNum = sortedNumList[index]
        smallerNum = sortedNumList[index - 1]
        if biggerNum - smallerNum == minDiff:
            lowestDifferenceNumbersList.append(smallerNum)
            lowestDifferenceNumbersList.append(biggerNum)
    return lowestDifferenceNumbersList


def main():
    sys.stdin = open('ClosestNumbers_input.txt')
    n = int(input().strip())
    listOfNumbers = list(map(int, input().strip().split(' ')))
    result = closestNumbers(listOfNumbers)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()

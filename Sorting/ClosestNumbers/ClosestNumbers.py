#!/bin/python3

import sys


def sortListOfNumbers(listOfNumbers):
    sortedListOfNumbers = []

    biggestNum = max(listOfNumbers)
    smallestNum = min(listOfNumbers)

    counter = [0] * (biggestNum - smallestNum + 1)

    for item in listOfNumbers:
        counter[item - smallestNum] += 1

    for index in range(0, len(counter)):
        for amount in range(0, counter[index]):
            sortedListOfNumbers.append(index + smallestNum)
    return sortedListOfNumbers


def closestNumbers(listOfNumbers):
    sortedNumList = sortListOfNumbers(listOfNumbers)

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

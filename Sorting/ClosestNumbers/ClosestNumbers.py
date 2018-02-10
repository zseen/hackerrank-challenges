#!/bin/python3

import sys


def sortListOfNumbers(listOfNumbers):
    sortedListOfNumbers = []

    biggestNum = max(listOfNumbers)
    smallestNum = min(listOfNumbers)

    if smallestNum < 0:
        counter = [0] * (biggestNum - smallestNum + 1)
    else:
        counter = [0] * (biggestNum + 1)

    for item in listOfNumbers:
        counter[item] += 1

    for index in range(smallestNum, biggestNum + 1):
        for amount in range(0, counter[index]):
            sortedListOfNumbers.append(index)
    return sortedListOfNumbers


def closestNumbers(listOfNumbers):
    sortedListOfNumbers = sortListOfNumbers(listOfNumbers)

    differenceBetweenNumbers = 1000000

    for index in range(1, len(sortedListOfNumbers)):
        biggerNum = sortedListOfNumbers[index]
        smallerNum = sortedListOfNumbers[index - 1]
        if biggerNum - smallerNum < differenceBetweenNumbers:
            differenceBetweenNumbers = biggerNum - smallerNum

    lowestDifferenceNumbersList = []

    for index in range(1, len(sortedListOfNumbers)):
        biggerNum = sortedListOfNumbers[index]
        smallerNum = sortedListOfNumbers[index - 1]
        if biggerNum - differenceBetweenNumbers == smallerNum:
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

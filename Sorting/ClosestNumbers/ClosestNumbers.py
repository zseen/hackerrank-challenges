#!/bin/python3

import sys

def closestNumbers(listOfNumbers):
    sortedListOfNumbers = []

    biggestNum = max(listOfNumbers)

    counter = [0] * (biggestNum + 1)

    for item in listOfNumbers:
        counter[item] += 1

    for index in range(0, biggestNum + 1):
        for amount in range(0, counter[index]):
            sortedListOfNumbers.append(index)

    differenceBetweenNumbers = 1000000

    for index in range(0, len(sortedListOfNumbers) + 1):
        if index < len(sortedListOfNumbers) - 1:
            if sortedListOfNumbers[index + 1] - sortedListOfNumbers[index] < differenceBetweenNumbers:
                differenceBetweenNumbers = sortedListOfNumbers[index + 1] - sortedListOfNumbers[index]
    return differenceBetweenNumbers


def main():
    sys.stdin = open('ClosestNumbers_input.txt')
    n = int(input().strip())
    listOfNumbers = list(map(int, input().strip().split(' ')))
    result = closestNumbers(listOfNumbers)
    #print (" ".join(map(str, result)))
    print(result)


if __name__ == "__main__":
    main()

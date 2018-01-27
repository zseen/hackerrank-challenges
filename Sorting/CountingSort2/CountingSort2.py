#!/bin/python3


import sys


def countingSort(listOfNumbers):
    sortedListOfNumbers = []

    biggestNum = max(listOfNumbers)

    counter = [0] * (biggestNum + 1)

    for item in listOfNumbers:
        counter[item] += 1

    for index in range(0, biggestNum + 1):
        for amount in range(0, counter[index]):
            sortedListOfNumbers.append(index)

    return sortedListOfNumbers


def main():
    sys.stdin = open('CountingSort2_input.txt')
    n = int(input().strip())
    listOfNumbers = list(map(int, input().strip().split(' ')))
    result = countingSort(listOfNumbers)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()

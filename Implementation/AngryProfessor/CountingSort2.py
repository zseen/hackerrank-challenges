#!/bin/python3


import sys


def countingSort(listOfNumbers):
    countList = []

    for i in range(0, 100):
        itemCount = listOfNumbers.count(i)
        for _ in range(0, itemCount):
            countList.append(i)

    return countList


def main():
    sys.stdin = open('CountingSort2_input.txt')
    n = int(input().strip())
    listOfNumbers = list(map(int, input().strip().split(' ')))
    result = countingSort(listOfNumbers)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()

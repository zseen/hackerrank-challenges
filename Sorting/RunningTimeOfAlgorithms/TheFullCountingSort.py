#!/bin/python3

import sys


def organiseStrings(allNumStrList):
    sortedListOfNumbers = []

    biggestNum = 0
    for item in allNumStrList:
        if item[0] > biggestNum:
            biggestNum = item[0]

    counter = []
    for _ in range(biggestNum + 1):
        counter.append([])

    for item in allNumStrList:
        counter[item[0]].append(item[1])

    for index in range(0, biggestNum + 1):
        for item in counter[index]:
            sortedListOfNumbers.append(item)

    print(sortedListOfNumbers)



    print(allNumStrList)


def main():
    sys.stdin = open('TheFullCountingSort_input.txt')
    n = int(input().strip())
    numStrTuple = ()
    allNumStrList = []


    for a0 in range(n):
        number, string = input().strip().split(' ')
        number, string = [int(number), str(string)]
        if a0 < n // 2:
            string = "-"
        numStrTuple = (number, string)
        allNumStrList.append(numStrTuple)


    organiseStrings(allNumStrList)


if __name__ == "__main__":
    main()


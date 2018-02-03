#!/bin/python3

import sys


def organiseStrings(allNumStrList):
    sortedListOfNumbers = []

    biggestNum = 0
    for item in allNumStrList:
        if item[0] > biggestNum:
            biggestNum = item[0]

    counter = [0] * (biggestNum + 1)

    for item in allNumStrList:
        counter[item[0]] += 1

    for index in range(0, biggestNum + 1):
        for amount in range(0, counter[index]):
            sortedListOfNumbers.append(index)

    print(sortedListOfNumbers)

    for item in sortedListOfNumbers:
        if item == 



    #print(allNumStrList)












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


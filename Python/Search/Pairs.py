#!/bin/python3

import sys


def pairs(difference, numbersList):
    pairsCounter = 0
    numbersDict = {}

    for item in numbersList:
        numbersDict[item] = item

    for key in numbersDict:
        if key + difference in numbersDict:
            pairsCounter += 1
    return pairsCounter


def main():
    sys.stdin = open("Pairs_input.txt")
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)
    print(result)

if __name__ == '__main__':
    main()

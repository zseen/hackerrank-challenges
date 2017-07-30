#!/bin/python3

import sys


def minMaxSum(numbersList):
    minList = []
    maxList = []
    for item in range(0, len(numbersList)-1):
        minList.append(numbersList[item])
        maxList.append(numbersList[len(numbersList)-1-item])

    minSum = (sum(minList))
    maxSum = (sum(maxList))
    return [minSum, maxSum]


def main():
    sys.stdin = open('mini-maxsum_input.txt')
    numbersList = list(map(int, input().strip().split(' ')))
    numbersList.sort()
    sums = minMaxSum(numbersList)
    print(sums[0], sums[1])


if __name__ == "__main__":
    main()

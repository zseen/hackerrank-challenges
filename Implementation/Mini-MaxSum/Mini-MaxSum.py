#!/bin/python3

import sys


def minMaxSum(numbersList):
    sortedList = sorted(numbersList)
    minList = []
    maxList = []
    for item in range(0, len(sortedList)-1):
        minList.append(sortedList[item])
        maxList.append(sortedList[len(sortedList)-1-item])



    minSum = (sum(minList))
    maxSum = (sum(maxList))
    return [minSum, maxSum]


def main():
    sys.stdin = open('Mini-MaxSum_input.txt')
    numbersList = list(map(int, input().strip().split(' ')))
    sums = minMaxSum(numbersList)
    print(sums[0], sums[1])


if __name__ == "__main__":
    main()

#!/bin/python3

import sys


def merge(left, right):
    counter = 0
    leftIndex = 0
    rightIndex = 0
    sortedList = []
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            sortedList.append(left[leftIndex])
            leftIndex += 1
        else:
            sortedList.append(right[rightIndex])
            rightIndex += 1
            counter += len(left) - leftIndex

    sortedList += left[leftIndex:]
    sortedList += right[rightIndex:]

    return sortedList, counter


def mergeSort(numbersList):
    if len(numbersList) <= 1:
        return numbersList, 0

    half = len(numbersList) // 2
    left, leftCounter = mergeSort(numbersList[:half])

    right, rightCounter = mergeSort(numbersList[half:])
    mergedList, mergedCounter = merge(left, right)

    return mergedList, rightCounter + leftCounter + mergedCounter


def main():
    sys.stdin = open('InsertionSortAdvancedAnalysis_input.txt')
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        numbersList = list(map(int, input().strip().split(' ')))
        result, resultCounter = mergeSort(numbersList)
        print(resultCounter)


if __name__ == "__main__":
    main()

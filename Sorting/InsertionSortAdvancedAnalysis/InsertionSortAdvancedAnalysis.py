#!/bin/python3

import sys


def merge(left, right):
    counter = 0
    leftIndex = 0
    rightIndex = 0
    sortedList = []
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            sortedList.append(left[leftIndex])
            leftIndex += 1
        else:
            sortedList.append(right[rightIndex])
            rightIndex += 1
            

    sortedList += left[leftIndex:]
    sortedList += right[rightIndex:]

    return sortedList


def mergeSort(numbersList):
    if len(numbersList) <= 1:
        return numbersList

    half = len(numbersList) // 2
    left = mergeSort(numbersList[:half])

    right = mergeSort(numbersList[half:])

    return merge(left, right)


def main():
    sys.stdin = open('InsertionSortAdvancedAnalysis_input.txt')
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        numbersList = list(map(int, input().strip().split(' ')))
        result = mergeSort(numbersList)
        print(result)


if __name__ == "__main__":
    main()

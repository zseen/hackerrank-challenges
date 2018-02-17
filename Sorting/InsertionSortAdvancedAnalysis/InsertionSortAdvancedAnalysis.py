#!/bin/python3

import sys

def mergeSort(listToBeSorted):
    counter = 0
    if len(listToBeSorted) > 1:
        mid = len(listToBeSorted) // 2
        leftHalf = listToBeSorted[:mid]
        rightHalf = listToBeSorted[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        leftListIndex = 0
        rightListIndex = 0
        originalListIndex = 0
        while leftListIndex < len(leftHalf) and rightListIndex < len(rightHalf):
            if leftHalf[leftListIndex] < rightHalf[rightListIndex]:
                listToBeSorted[originalListIndex] = leftHalf[leftListIndex]
                leftListIndex += 1
                counter += 1
            else:
                listToBeSorted[originalListIndex] = rightHalf[rightListIndex]
                rightListIndex += 1
                counter += 1
            originalListIndex += 1

        while leftListIndex < len(leftHalf):
            listToBeSorted[originalListIndex] = leftHalf[leftListIndex]
            leftListIndex += 1
            originalListIndex += 1

        while rightListIndex < len(rightHalf):
            listToBeSorted[originalListIndex] = rightHalf[rightListIndex]
            rightListIndex += 1
            originalListIndex += 1
    return listToBeSorted




if __name__ == "__main__":
    sys.stdin = open('InsertionSortAdvancedAnalysis_input.txt')
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        numbersList = list(map(int, input().strip().split(' ')))
        result = mergeSort(numbersList)
        print(result)
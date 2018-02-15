#!/bin/python3

import sys

def insertionSort(listToBeSorted):
    counter = 0




if __name__ == "__main__":
    sys.stdin = open('InsertionSortAdvancedAnalysis_input.txt')
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        numbersList = list(map(int, input().strip().split(' ')))
        result = insertionSort(numbersList)
        print(result)
#!/bin/python3

import sys


def returnAsString(list):
    return ' '.join(str(i) for i in list)


def quickSort(listToDivide):
    p = listToDivide[0]
    right = []
    left = []


    for item in listToDivide:
        if item > p:
            right.append(item)
        elif item < p:
            left.append(item)

    l = returnAsString(left)
    r = returnAsString(right)

    return l, p, r

if __name__ == "__main__":
    sys.stdin = open('Quicksort1 - Partition_input.txt')
    n = int(input().strip())
    listToDivide = list(map(int, input().strip().split(' ')))
    result = quickSort(listToDivide)
    print(" ".join(map(str, result)))


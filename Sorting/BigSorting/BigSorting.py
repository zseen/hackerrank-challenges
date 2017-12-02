#!/bin/python3

import sys


def getSortedList(unsortedList):
    return sorted(unsortedList, key=int)


def main():
    sys.stdin = open('BigSorting_input.txt')
    n = int(input().strip())
    unsorted = []

    for _ in range(n):
        unsorted_t = str(input().strip())
        unsorted.append(unsorted_t)
    sortedList = getSortedList(unsorted)

    for item in sortedList:
        print(item)

if __name__ == "__main__":
    main()

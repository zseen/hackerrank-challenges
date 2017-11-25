#!/bin/python3

import sys


def getSortedList(n):
    unsorted = []

    for _ in range(n):
        unsorted_t = str(input().strip())
        unsorted.append(unsorted_t)
    return sorted(unsorted, key=int)


def main():
    sys.stdin = open('bigSorting_input.txt')
    n = int(input().strip())
    sortedList = getSortedList(n)

    for item in sortedList:
        print(item)

if __name__ == "__main__":
    main()

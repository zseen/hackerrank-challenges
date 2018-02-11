#!/bin/python3


import sys
from Library.Sorting import CountingSort


def main():
    sys.stdin = open('CountingSort2_input.txt')
    n = int(input().strip())
    listOfNumbers = list(map(int, input().strip().split(' ')))
    result = CountingSort.sortListOfNumbers(listOfNumbers)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()

#!/bin/python3

import sys
from collections import Counter


def sockMerchant(n, listOfSocks):
    countPairs = 0
    numberOfSocks = Counter(listOfSocks).most_common()

    for item in numberOfSocks:
        if item[1] == 1:
            return countPairs
        elif item[1] % 2 == 0:
            countPairs += item[1] // 2
        else:
            countPairs += (item[1] - 1) // 2
    return countPairs


def main():
    sys.stdin = open('sockMerchant_input.txt')
    n = int(input().strip())
    listOfSocks = list(map(int, input().strip().split(' ')))
    result = sockMerchant(n, listOfSocks)
    print(result)

if __name__ == "__main__":
    main()



#!/bin/python3

import sys
from collections import Counter


def sockMerchant(listOfSocks):
    countPairs = 0

    counter = Counter()
    for sock in listOfSocks:
        counter[sock] += 1

    for key,value in counter.items():
        countPairs += value // 2

    return countPairs


def main():
    sys.stdin = open('SockMerchant_input.txt')
    n = int(input().strip())
    listOfSocks = list(map(int, input().strip().split(' ')))
    result = sockMerchant(listOfSocks)
    print(result)

if __name__ == "__main__":
    main()



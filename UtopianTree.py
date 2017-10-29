#!/bin/python3

import sys


def growthHalfCycle(n):
    currHeight = growthFullCycle(n - 1)
    return currHeight * 2


def growthFullCycle(n):
    if n % 2 != 0:
        raise RuntimeError("Method can only be called with an even parameter")
    currentHeight = 1
    for _ in range(0, n//2):
        currentHeight *= 2
        currentHeight += 1
    return currentHeight


def getHeight(n):
    treeHeights = []

    if n % 2 == 0:
        treeHeight = growthFullCycle(n)
    else:
        treeHeight = growthHalfCycle(n)
    treeHeights.append(treeHeight)

    return treeHeights


def main():
    sys.stdin = open('utopianTree_input.txt')
    t = int(input().strip())

    for a0 in range(t):
        n = int(input().strip())
        height = getHeight(n)
        for item in height:
            print(item)

if __name__ == "__main__":
    main()


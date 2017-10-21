#!/bin/python3

import sys

def growthHalfCycle(n):
    cH = growthFullCycle(n)
    return cH * 2

def growthFullCycle(n):
    currentHeight = 1
    for currentHeight in range(0,(n//2)+1):
        currentHeight = currentHeight * 2
        currentHeight += 1
    return currentHeight


def getHeight(n):

    treeFull = growthFullCycle(n)
    treeHalf = growthHalfCycle(n)

    if n % 2 == 0:
        return treeFull
    else:
        return treeHalf



            #if n == 4:
            #1*2 , 1*2+1
            #3*2 , 3*2+1
            #if n == 5:
            #1*2 , 1*2+1
            #3*2 , 3*2+1
            #(3*2+1)

def main():
    sys.stdin = open('utopianTree_input.txt')
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(n)
    height = getHeight(t)

    print(height)

if __name__ == "__main__":
    main()


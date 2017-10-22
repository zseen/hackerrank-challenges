#!/bin/python3

import sys


def growthHalfCycle(n):
    currHeight = growthFullCycle(n)
    return currHeight * 2

def growthFullCycle(n):
    currentHeight = 1
    for i in range(1,(n//2)+1):
        currentHeight = currentHeight * 2
        currentHeight += 1
    return currentHeight


def getHeight(n):



    treeHeights = []

    if n % 2 == 0:
        treeFull = growthFullCycle(n)
        treeHeights.append(treeFull)
    else:
        treeHalf = growthHalfCycle(n)
        treeHeights.append(treeHalf)

    return treeHeights



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
        #print(n)

        height = getHeight(n)

        for item in height:
            print(item)

if __name__ == "__main__":
    main()


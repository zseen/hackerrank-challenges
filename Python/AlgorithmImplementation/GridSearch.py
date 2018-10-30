import math
import os
import random
import re
import sys


def gridSearch(grid, pattern):
    gridHeight = len(grid)
    patternHeight = len(pattern)

    for i in range(gridHeight - patternHeight + 1):
        if pattern[0] in grid[i]:
            patternInGridStartIndexSet = getPatternMatch(grid, i, pattern, 0)
            for index in range(len(pattern)):
                patternInGridStartIndexSet = getIndexesIntersection(grid, i, index, pattern, patternInGridStartIndexSet)
            if len(patternInGridStartIndexSet) == 1:
                return True
    else:
        return False


def getIndexesIntersection(grid, gridIndex, patternIndex, pattern, patternRowsStartSet):
    patternRowsStartSet = patternRowsStartSet.intersection(set(x.start() for x in
                                    re.finditer('(?=' + pattern[patternIndex] + ')', grid[gridIndex + patternIndex])))
    return patternRowsStartSet


def getPatternMatch(grid, gridIndex, pattern, patternIndex):
    patternInGridStartIndexSet = set(x.start() for x in re.finditer('(?=' + pattern[patternIndex] + ')', grid[gridIndex]))
    return patternInGridStartIndexSet


def printReturnCases(grid, pattern):
    state = gridSearch(grid, pattern)
    if state:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    sys.stdin = open("TestCase5.txt")

    testCasesNum = int(input())

    for t_itr in range(testCasesNum):
        RC = input().split()


        rowsInGrid = int(RC[0])

        columnsInGrid = int(RC[1])

        gridList = []

        for _ in range(rowsInGrid):
            G_item = input()
            gridList.append(G_item)

        rc = input().split()

        linesNumInGrid = int(rc[0])

        digitsInGrid = int(rc[1])

        patternList = []

        for _ in range(linesNumInGrid):
            P_item = input()
            patternList.append(P_item)

        printReturnCases(gridList, patternList)

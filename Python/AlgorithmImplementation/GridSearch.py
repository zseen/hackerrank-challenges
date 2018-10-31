import math
import os
import random
import re
import sys


def gridSearch(grid, pattern):
    gridHeight = len(grid)
    patternHeight = len(pattern)

    for patternStartRowIndex in range(gridHeight - patternHeight + 1):
        patternInGridStartIndexSet = getAllSubstringStartIndices(pattern[0], grid[patternStartRowIndex])
        for patternRowOffset in range(len(pattern)):
            patternInGridStartIndexSet = patternInGridStartIndexSet.intersection(getAllSubstringStartIndices(pattern[patternRowOffset], grid[patternStartRowIndex + patternRowOffset]))
            if len(patternInGridStartIndexSet) == 0:
                break
        if len(patternInGridStartIndexSet) >= 1:
            return True
    else:
        return False


def getAllSubstringStartIndices(string, subString):
    patternInGridStartIndexSet = set(x.start() for x in re.finditer('(?=' + string + ')', subString))
    return patternInGridStartIndexSet


def printGridSearch(grid, pattern):
    result = gridSearch(grid, pattern)
    if result:
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

        printGridSearch(gridList, patternList)

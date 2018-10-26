import math
import os
import random
import re
import sys


def gridSearch(grid, pattern):
    for j in range(0, len(grid[0]) - len(pattern[0]) + 1):
        print(j)
        for i in range(0, len(grid) - len(pattern) + 1):
            good = True
            for y in range(0, len(pattern[0])):
                for x in range(0, len(pattern)):
                    if grid[i + x][j + y] != pattern[x][y]:
                        good = False
                        break
            if good:
                return "YES"
    return "NO"





if __name__ == '__main__':
    sys.stdin = open("GridSearch_input.txt")

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

        result = gridSearch(gridList, patternList)



        print(result)

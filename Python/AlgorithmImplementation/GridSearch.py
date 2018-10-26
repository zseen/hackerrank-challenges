import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(grid, pattern):
    #print(grid)
    l = len(grid)
    k = len(grid[0])
    v = len(pattern)
    o = len(pattern[0])

    for i in range(0, len(grid) - len(pattern) + 1):
        for j in range(0, len(grid[0]) - len(pattern[0]) + 1):
            good = True
            for x in range(0, len(pattern)):
                for y in range(0, len(pattern[0])):
                    p = (grid[i + x][j + y])
                    pp = (pattern[x][y])
                    if grid[i + x][j + y] != pattern[x][y]:

                        good = False
                        break
            if good:
                return True
    return False





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

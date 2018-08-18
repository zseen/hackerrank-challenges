import math
import os
import random
import re
import sys


def takeTurnsGetWinner(listOfNums):

    maxItem = listOfNums[0]
    countTurns = 1

    for i in range(1, len(listOfNums)):
        if listOfNums[i] > maxItem:
            maxItem = listOfNums[i]
            countTurns += 1

    if countTurns % 2 == 0:
        return "ANDY"

    return "BOB"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        arr_count = int(input())

        numsList = list(map(int, input().rstrip().split()))

        result = takeTurnsGetWinner(numsList)

        fptr.write(str(result) + '\n')

    fptr.close()

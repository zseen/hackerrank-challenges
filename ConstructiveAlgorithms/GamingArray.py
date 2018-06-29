import math
import os
import random
import re
import sys

# Complete the gamingArray function below.


def takeTurns(listForTurn):
    countTurns = 0


    while len(listForTurn) > 0:
        listForTurn = getMaxItemAndDeleteRight(listForTurn)
        countTurns += 1

    if countTurns % 2 == 0:
        return "ANDY"

    return "BOB"




def getMaxItemAndDeleteRight(numsList):
    #maxItem = 0
    #maxItemIndex = 0

    # for i in range(0, len(numsList)):
    #     if numsList[i] > maxItem:
    #         maxItem = numsList[i]
    #         maxItemIndex = i


    maxItem = numsList[0]
    maxItemIndex = 0

    for i in range(1, len(numsList)):
        if numsList[i] > maxItem:
            #maxItem = numsList[i]
            maxItemIndex = i

    numsList = numsList[0: maxItemIndex]

    return numsList





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        arr_count = int(input())

        numsList = list(map(int, input().rstrip().split()))

        result = takeTurns(numsList)


        fptr.write(str(result) + '\n')

    fptr.close()
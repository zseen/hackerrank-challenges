import math
import os
import random
import re
import sys


LOCAL_INPUT = True

print(22222)

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

def getTurnsInput():
    arr_count = int(input())
    numsList = list(map(int, input().rstrip().split()))
    result = takeTurnsGetWinner(numsList)
    print(333333333333333333)
    return result

def main():
    g = int(input())
    print(22222222222222222222222222222222222222222222222222222222222222222222222222222222222222)
    if LOCAL_INPUT is True:
        print(222222222222222222222222222222222)
        sys.stdin = open('GamingArray_input.txt')
        for g_itr in range(g):
            result = getTurnsInput()
            print(result)
    else:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        for g_itr in range(g):
            result = getTurnsInput()
            fptr.write(str(result) + '\n')
        fptr.close()

if __name__ == '__main__':
    main()

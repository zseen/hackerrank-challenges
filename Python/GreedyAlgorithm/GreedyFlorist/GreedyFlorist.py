#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(friendsNum, flowersPricesList):
    flowersPricesList = list(reversed(sorted(flowersPricesList)))
    purchasingFriendID = 0
    moneySpentTotal = 0
    round = 0
    stem = 1

    for price in flowersPricesList:
        moneySpentTotal += price * (round + stem)

        purchasingFriendID += 1
        if purchasingFriendID == friendsNum:
            purchasingFriendID = 0
            round += 1

    return moneySpentTotal



if __name__ == '__main__':
    sys.stdin = open("GreedyFlorist_input.txt")

    nk = input().split()
    flowersNum = int(nk[0])
    friendsNum = int(nk[1])
    flowersPricesList = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(friendsNum, flowersPricesList)
    print(minimumCost)

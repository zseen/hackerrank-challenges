#!/bin/python3

import sys


def saveThePrisoner(numberOfPrisoners, numberOfSweets, prisonerID):
    remainingSweets = numberOfSweets % numberOfPrisoners

    if prisonerID + remainingSweets > numberOfPrisoners:
        warned = remainingSweets - (numberOfPrisoners - prisonerID) - 1
    else:
        warned = prisonerID + remainingSweets - 1
    return warned if warned != 0 else numberOfPrisoners


sys.stdin = open('saveThePrisoner_input.txt')
t = int(input().strip())
for a0 in range(t):
    numberOfPrisoners, numberOfSweets, prisonerID = input().strip().split(' ')
    numberOfPrisoners, numberOfSweets, prisonerID = [int(numberOfPrisoners), int(numberOfSweets), int(prisonerID)]
    result = saveThePrisoner(numberOfPrisoners, numberOfSweets, prisonerID)
    print(result)

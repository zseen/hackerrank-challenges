#!/bin/python3

import sys


def saveThePrisoner(numberOfPrisoners, numberOfSweets, prisonerID):
    if numberOfSweets > numberOfPrisoners:
        x = numberOfSweets % numberOfPrisoners
        if x + prisonerID > numberOfPrisoners:
            warned = numberOfPrisoners - x - 1
            return warned
        warned = prisonerID + x - 1

    else:
        warned = prisonerID + numberOfSweets - 1

    return warned


sys.stdin = open('saveThePrisoner_input.txt')
t = int(input().strip())
for a0 in range(t):
    numberOfPrisoners, numberOfSweets, prisonerID = input().strip().split(' ')
    numberOfPrisoners, numberOfSweets, prisonerID = [int(numberOfPrisoners), int(numberOfSweets), int(prisonerID)]
    result = saveThePrisoner(numberOfPrisoners, numberOfSweets, prisonerID)
    print(result)

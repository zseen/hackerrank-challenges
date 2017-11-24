#!/bin/python3

import sys


def getPrisonerIDToWarn(numberOfPrisoners, numberOfSweets, prisonerID):
    remainingSweets = numberOfSweets % numberOfPrisoners

    firstIndexToGet = prisonerID - 1
    lastIndexToGet = (firstIndexToGet + remainingSweets - 1) % numberOfPrisoners

    return lastIndexToGet + 1

def main():
    sys.stdin = open('saveThePrisoner_input.txt')
    t = int(input().strip())
    for a0 in range(t):
        numberOfPrisoners, numberOfSweets, prisonerID = input().strip().split(' ')
        numberOfPrisoners, numberOfSweets, prisonerID = [int(numberOfPrisoners), int(numberOfSweets), int(prisonerID)]
        result = getPrisonerIDToWarn(numberOfPrisoners, numberOfSweets, prisonerID)
        print(result)

if __name__ == "__main__":
    main()

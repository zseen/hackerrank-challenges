#!/bin/python3

import sys


def solve1(numberOfSquares, digitOnSquares, day, month):
    canGive = 0
    for itemNumber in range(0, numberOfSquares):
        if sum(digitOnSquares[itemNumber:itemNumber+month:]) == day:
            canGive += 1
    return canGive


def solve2(numberOfSquares, digitOnSquares, day, month):
    canGive = 0

    for itemNumber in range(0, (numberOfSquares-month)+1):
        currentSum = 0
        for index in range(0, month):
            currentSum += digitOnSquares[itemNumber+index]
        if currentSum == day:
            canGive += 1

    return canGive


def main():
    sys.stdin = open('BirthdayChocolate_input.txt')
    numberOfSquares = int(input().strip())
    digitOnSquares = list(map(int, input().strip().split(' ')))
    day, month = input().strip().split(' ')
    day, month = [int(day), int(month)]
    #result = solve1(numberOfSquares, digitOnSquares, day, month)
    result = solve2(numberOfSquares, digitOnSquares, day, month)
    print(result)


if __name__ == '__main__':
    main()


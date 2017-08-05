#!/bin/python3

import sys


def solve(numberOfSquares, digitOnSquares, day, month):
    canGive = 0

    if numberOfSquares == 1:
        if day == digitOnSquares[0]:
            canGive += 1

    for itemNumber in range(0, numberOfSquares-1):
        if sum(digitOnSquares[itemNumber:itemNumber+month:]) == day:
            canGive += 1

    return canGive


def main():
    sys.stdin = open('birthdayChocolate_input.txt')
    numberOfSquares = int(input().strip())
    digitOnSquares = list(map(int, input().strip().split(' ')))
    day, month = input().strip().split(' ')
    day, month = [int(day), int(month)]
    result = solve(numberOfSquares, digitOnSquares, day, month)
    print(result)


if __name__ == '__main__':
    main()


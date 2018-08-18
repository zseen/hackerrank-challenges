#!/bin/python3

import sys


def possibleMagicSquares():
    listOfSquares = []
    with open('FormingAMagicSquare_squares.txt') as file:
        line = file.readline()
        while line:
            square = []
            for s_i in range(3):
                s_t = [int(s_temp) for s_temp in line.strip().split(' ')]
                square.append(s_t)

                line = file.readline()
            listOfSquares.append(square)
    return listOfSquares


def getMinimalCostDifference(square, magicSquares):
    minimalCost = sys.maxsize
    for item in magicSquares:
        cost = getCostDifference(item, square)
        if cost < minimalCost:
            minimalCost = cost
    return minimalCost


def getCostDifference(item, square):
    costOfItems = 0
    for i in range(0, 3):
        for e in range(0, 3):
            costOfItems += abs(item[i][e] - square[i][e])

    return costOfItems


def main():
    sys.stdin = open('FormingAMagicSquare_input.txt')
    square = []
    for s_i in range(3):
        s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
        square.append(s_t)
    # Print the minimum cost of converting 's' into a magic square
    try:
        possibleSquares = possibleMagicSquares()
        cost = getMinimalCostDifference(square, possibleSquares)
        print(cost)
    except ValueError as ve:
        print("Your file format is invalid, please check it: " + str(ve))

if __name__ == "__main__":
    main()


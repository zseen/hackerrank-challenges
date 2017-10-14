#!/bin/python3

import sys


def possibleMagicSquares():
    magicSquares = []
    magicSquares.append([[8,1,6],[3,5,7],[4,9,2]])
    magicSquares.append([[6,1,8],[7,5,3],[2,9,4]])
    magicSquares.append([[4,9,2],[3,5,7],[8,1,6]])
    magicSquares.append([[2,9,4],[7,5,3],[6,1,8]])
    magicSquares.append([[8,3,4],[1,5,9],[6,7,2]])
    magicSquares.append([[4,3,8],[9,5,1],[2,7,6]])
    magicSquares.append([[6,7,2],[1,5,9],[8,3,4]])
    magicSquares.append([[2,7,6],[9,5,1],[4,3,8]])

    return magicSquares


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
    sys.stdin = open('formingAMagicSquare_input.txt')
    square = []
    for s_i in range(3):
        s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
        square.append(s_t)
    # Print the minimum cost of converting 's' into a magic square
    possibleSquares = possibleMagicSquares()
    cost = getMinimalCostDifference(square, possibleSquares)
    print(cost)

if __name__ == "__main__":
    main()


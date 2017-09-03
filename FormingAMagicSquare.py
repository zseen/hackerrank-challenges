#!/bin/python3

import sys

def sumVertical(square):
    sumVert1 = 0
    sumVert2 = 0
    sumVert3 = 0
    for item in square:
        sumVert1 += item[0]
        sumVert2 += item[1]
        sumVert3 += item[2]

    if sumVert1 != 15 or sumVert2 != 15 or sumVert3 != 15:
        return False
    return True


def sumHorizontal(square):
    sumHor1 = sum(square[0])
    sumHor2 = sum(square[1])
    sumHor3 = sum(square[2])

    if sumHor1 != 15 or sumHor2 != 15 or sumHor3 != 15:
        return False
    return True


def sumDiagonal(square):
    diag1 = [square[0][0], square[1][1], square[2][2]]
    diag2 = [square[0][2], square[1][1], square[2][0]]
    if sum(diag1) != 15 or sum(diag2) != 15:
        return False
    return True


def checkIfMagicSquare(square):
    diag = sumDiagonal(square)
    horiz = sumHorizontal(square)
    vertic = sumVertical(square)

    if diag == False or horiz == False or vertic == False:
        return "Not magic"


def makeMagicSquare(square):






sys.stdin = open('formingAMagicSquare_input.txt')
square = []
for s_i in range(3):
   s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
   square.append(s_t)
#  Print the minimum cost of converting 's' into a magic square

x = checkIfMagicSquare(square)
print(x)
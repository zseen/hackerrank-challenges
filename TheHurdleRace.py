#!/bin/python3

import sys

sys.stdin = open('theHurdleRace_input.txt')
numberOfHurdles, maxJumpHeight = input().strip().split(' ')
numberOfHurdles, maxJumpHeight = [int(numberOfHurdles), int(maxJumpHeight)]
height = list(map(int, input().strip().split(' ')))

def beveragesToDrink():
    #print(maxJumpHeight)
    #print(height)
    beverage = 0
    for item in height:
        if item + beverage > maxJumpHeight:
            beverage += item - maxJumpHeight
    print(beverage)

beveragesToDrink()
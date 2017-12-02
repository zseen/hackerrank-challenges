#!/bin/python3

import sys


def beveragesToDrink(maxJumpHeight, height):
    beverage = 0
    for item in height:
        if item > maxJumpHeight + beverage:
            beverage = item - maxJumpHeight
    return beverage

def main():
    sys.stdin = open('TheHurdleRace_input.txt')
    numberOfHurdles, maxJumpHeight = input().strip().split(' ')
    numberOfHurdles, maxJumpHeight = [int(numberOfHurdles), int(maxJumpHeight)]
    height = list(map(int, input().strip().split(' ')))
    drink = beveragesToDrink(maxJumpHeight, height)
    print(drink)


if __name__ == "__main__":
    main()
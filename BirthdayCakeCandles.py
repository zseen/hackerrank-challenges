#!/bin/python3

import sys


def birthdayCakeCandles(candleHeight):
    candleHeight.sort()
    height = candleHeight[::-1]
    
    sameHeight = 0
    for item in range(0, len(height)):
        sameHeight += 1
        if item == len(height) - 1 or height[item] != height[item + 1]:
            break

    return sameHeight


def main():
    sys.stdin = open('birthdaycakecandles_input.txt')
    age = int(input().strip())
    candleHeight = list(map(int, input().strip().split(' ')))
    result = birthdayCakeCandles(candleHeight)
    print(result)


if __name__ == "__main__":
    main()


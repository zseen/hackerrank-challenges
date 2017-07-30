#!/bin/python3

import sys


def birthdayCakeCandles(candleHeight):
    candleHeight.sort()
    height = candleHeight[::-1]
    sameHeight = []
    for item in range(0, len(height)):
        if item == len(height)-1:
            sameHeight.append(height[item])
            break
        elif height[item] == height[item+1]:
            sameHeight.append(height[item])
        elif height[item] != height[item+1]:
            sameHeight.append(height[item])
            break

    return len(sameHeight)


def main():
    sys.stdin = open('birthdaycakecandles_input.txt')
    #age = int(input().strip())
    candleHeight = list(map(int, input().strip().split(' ')))
    result = birthdayCakeCandles(candleHeight)
    print(result)


if __name__ == "__main__":
    main()


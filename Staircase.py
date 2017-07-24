#!/bin/python3

import sys


def staircase(numberOfStairs):
    stairs = numberOfStairs - 1
    for x in range(1, numberOfStairs):
        print(' ' * (numberOfStairs-x-1), '#' * x)
        stairs -= 1
    print('#' * numberOfStairs)


def main():
    sys.stdin = open('staircase_input.txt')
    numberOfStairs = int(input().strip())
    staircase(numberOfStairs)

if __name__ == "__main__":
    main()


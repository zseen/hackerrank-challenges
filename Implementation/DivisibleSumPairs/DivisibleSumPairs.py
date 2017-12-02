#!/bin/python3

import sys


def divisibleSumPairs(n, divisor, numbers):
    pairs = 0
    for numberOne in range(0, n-1):
        for numberTwo in range(numberOne+1,n):
            if (numbers[numberOne] + numbers[numberTwo]) % divisor == 0:
                pairs += 1

    return pairs


def main():
    sys.stdin = open('DivisibleSumPairs_input.txt')
    n, divisor = input().strip().split(' ')
    n, divisor = [int(n), int(divisor)]
    numbers = list(map(int, input().strip().split(' ')))
    result = divisibleSumPairs(n, divisor, numbers)
    print(result)

if __name__ == "__main__":
    main()




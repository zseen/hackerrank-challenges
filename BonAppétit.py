#!/bin/python3

import sys

def bonAppetit(n, didNotEat, annaCharged, prices):
    sumWithoutDidNotEat = (sum(prices)-prices[didNotEat])/2

    if annaCharged == sumWithoutDidNotEat:
        return True

    return False


def main():
    sys.stdin = open('bonAppétit_input.txt')
    n, didNotEat = input().strip().split(' ')
    n, didNotEat = [int(n), int(didNotEat)]
    prices = list(map(int, input().strip().split(' ')))
    annaCharged = int(input().strip())
    result = bonAppetit(n, didNotEat, annaCharged, prices)
    if result is True:
        print("Bon Appetit")
    else:
        print(int(annaCharged - (sum(prices)-prices[didNotEat])/2))

if __name__ == "__main__":
    main()



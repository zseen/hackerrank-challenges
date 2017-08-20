#!/bin/python3

import sys


class BetweenTheSets(object):
    def __init__(self, smallNumbers, bigNumbers):
        self.smallNumbers = smallNumbers
        self.bigNumbers = bigNumbers

    @staticmethod
    def numberDividedByElements(numberToDivide, listOfNumbers):
        for element in listOfNumbers:
            if numberToDivide % element != 0:
                return False
        return True

    @staticmethod
    def elementsDividedByDivisor(divisor, listOfNumbers):
        for element in listOfNumbers:
            if element % divisor != 0:
                return False
        return True

    def getBetweenTwoSetsCount(self):
        counter = 0

        biggestInA = max(self.smallNumbers)
        smallestInB = min(self.bigNumbers)

        for item in range(biggestInA, smallestInB + 1):
            numberA = BetweenTheSets.numberDividedByElements(item, self.smallNumbers)
            numberB = BetweenTheSets.elementsDividedByDivisor(item, self.bigNumbers)
            if numberA is True and numberB is True:
                counter += 1

        return counter


def main():
    sys.stdin = open('betweenTwoSets_input.txt')
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    bts = BetweenTheSets(a, b)
    total = bts.getBetweenTwoSetsCount()

    print(total)

if __name__ == "__main__":
    main()



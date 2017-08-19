#!/bin/python3

import sys


def numberDividedByElements(numberToDivide, listOfNumbers):
    for element in listOfNumbers:
        if numberToDivide % element != 0:
            return False
    return True


def elementsDividedByDivisor(divisor, listOfNumbers):
    for element in listOfNumbers:
        if element % divisor != 0:
            return False
    return True


def getBetweenTwoSetsCount(smallNumbers, bigNumbers):
    counter = 0

    biggestInA = max(smallNumbers)
    smallestInB = min(bigNumbers)

    for item in range(biggestInA, smallestInB + 1):
        numberA = numberDividedByElements(item, smallNumbers)
        numberB = elementsDividedByDivisor(item, bigNumbers)
        if numberA is True and numberB is True:
            counter += 1

    return counter


def main():
    sys.stdin = open('betweenTwoSets_input.txt')
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getBetweenTwoSetsCount(a, b)
    print(total)



if __name__ == "__main__":
    main()



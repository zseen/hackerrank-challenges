#!/bin/python3

import sys
from WaiterPrimes import first1200Primes as primes


def waiter(numbersList, iterNum):
    divisibleNums = []
    numsOrderForPrintingList = []
    remainingNumbersList = []

    for index in range(0, iterNum):
        remainingNumbersList = []
        currentDivisibleNums = []
        divisibleNums.append(currentDivisibleNums)
        while len(numbersList) != 0:
            currentNum = numbersList.pop()
            if currentNum % primes[index] == 0:
                currentDivisibleNums.append(currentNum)
            else:
                remainingNumbersList.append(currentNum)
        numbersList = remainingNumbersList

    for subList in divisibleNums:
        while len(subList) != 0:
            numsOrderForPrintingList.append(subList.pop())

    numsOrderForPrintingList.extend(reversed(remainingNumbersList))

    return numsOrderForPrintingList


def main():
    sys.stdin = open("Waiter_input.txt")
    nq = input().split()
    n = int(nq[0])
    iterationsNum = int(nq[1])
    numbersList = list(map(int, input().rstrip().split()))

    result = waiter(numbersList, iterationsNum)
    print(result)


if __name__ == '__main__':
    main()

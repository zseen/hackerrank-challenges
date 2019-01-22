#!/bin/python3

import sys
from WaiterPrimes import first1200Primes as primes


def waiter(numbersList, iterNum):
    divisibleNums = []
    numsOrderForPrintingList = []

    for index in range(0, iterNum):
        remainingNumbersList = numbersList
        numbersList = []
        divisibleNums.append([])
        while len(remainingNumbersList) != 0:
            currentNum = remainingNumbersList.pop()
            if currentNum % primes[index] == 0:
                divisibleNums[index].append(currentNum)
            else:
                numbersList.append(currentNum)

    for subList in divisibleNums:
        while len(subList) != 0:
            numsOrderForPrintingList.append(subList.pop())

    numsOrderForPrintingList.extend(reversed(numbersList))

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

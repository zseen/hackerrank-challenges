#!/bin/python3

import sys
from Waiter_primes import first1200Primes


def waiter(numbersList, iterNum):
    divisibleNums = []
    remainingNumbers = numbersList
    numsOrderForPrintingList = []
    primes = first1200Primes

    for index in range(0, iterNum):
        tempNumsList = remainingNumbers
        remainingNumbers = []
        divisibleNums.append([])
        while len(tempNumsList) != 0:
            currentNum = tempNumsList.pop()
            if currentNum % primes[index] == 0:
                divisibleNums[index].append(currentNum)
            else:
                remainingNumbers.append(currentNum)

    for subList in divisibleNums:
        while len(subList) != 0:
            numsOrderForPrintingList.append(subList.pop())

    numsOrderForPrintingList.extend(reversed(remainingNumbers))

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

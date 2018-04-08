#!/bin/python3

import sys
from Library.Sorting import CountingSort


def getNumCounter(moneySpentDaily, daysPrior):
    daysPriorSpent = []
    for index in range(0, daysPrior):
        daysPriorSpent.append(moneySpentDaily[index])

    biggestNum = max(daysPriorSpent)
    smallestNum = min(daysPriorSpent)

    counter = [0] * (biggestNum - smallestNum + 1)

    for item in daysPriorSpent:
        counter[item - smallestNum] += 1

    return counter


def daysPriorIsOddMedian(moneySpentDaily, daysPrior):
    medianItem = (daysPrior // 2) + 1
    listSum = 0
    counter = getNumCounter(moneySpentDaily, daysPrior)
    for item in counter:
        listSum += item
        if listSum >= medianItem:
            median = medianItem
            return median


def daysPriorIsEvenMedian(moneySpentDaily, daysPrior):
    medianItem1 = daysPrior // 2
    medianItem2 = daysPrior // 2 + 1
    medianItemAv = (medianItem1 + medianItem2) / 2
    listSum = 0
    counter = getNumCounter(moneySpentDaily, daysPrior)
    for item in counter:
        listSum += item
        if listSum >= medianItemAv:
            median = medianItemAv
            return median







def main():
    sys.stdin = open('FraudulentActivityNotifications_input.txt')
    daysNumData, daysPrior = input().strip().split(' ')
    daysNumData, daysPrior = [int(daysNumData), int(daysPrior)]
    moneySpentDaily = list(map(int, input().strip().split(' ')))
    if daysPrior % 2 != 0:
        result = daysPriorIsOddMedian(moneySpentDaily, daysPrior)
        print(result)
    result = daysPriorIsEvenMedian(moneySpentDaily, daysPrior)
    print(result)


if __name__ == "__main__":
    main()

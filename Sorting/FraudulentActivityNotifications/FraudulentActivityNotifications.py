#!/bin/python3

import sys
from Library.Sorting import CountingSort as cs


def activityNotifications(moneySpentDaily, daysPrior):
    moneySpentForDaysPrior = []
    for index in range(0, len(moneySpentDaily) - daysPrior):
        for i in range(0, daysPrior):
            moneySpentForDaysPrior.append(moneySpentDaily[index + i])
    print(moneySpentForDaysPrior)

    subListMoneySpentPrior = [moneySpentForDaysPrior[n:n + 5] for n in range(0, len(moneySpentForDaysPrior), 5)]
    #print(subListMoneySpentPrior)

    counter = 0

    for index in range(1, len(subListMoneySpentPrior)):
        sortedDailySpent = cs.sortListOfNumbers(subListMoneySpentPrior[index])
        medianSpent = sortedDailySpent[len(sortedDailySpent) // 2]
        if medianSpent < moneySpentDaily[index + 5]:
            counter += 1
    return counter


if __name__ == "__main__":
    sys.stdin = open('FraudulentActivityNotifications_input.txt')
    daysNumData, daysPrior = input().strip().split(' ')
    daysNumData, daysPrior = [int(daysNumData), int(daysPrior)]
    moneySpentDaily = list(map(int, input().strip().split(' ')))
    result = activityNotifications(moneySpentDaily, daysPrior)
    print(result)
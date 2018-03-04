#!/bin/python3

import sys
from Library.Sorting import CountingSort as cs


def activityNotifications(moneySpentDaily, daysPrior):
    notificationsCount = 0
    daysPriorIndex = daysPrior - 1
    initialMedianSpent = 0
    initialMedianSpentList = []
    for i in range(0, daysPrior):
        initialMedianSpentList.append(moneySpentDaily[i])



    moneySpentForDaysPrior = []
    for index in range(0, len(moneySpentDaily) - daysPrior):

        for i in range(0, daysPrior):
            moneySpentForDaysPrior.append(moneySpentDaily[index + i])
    #print(moneySpentForDaysPrior)

    subListMoneySpentPrior = [moneySpentForDaysPrior[n:n + 5] for n in range(0, len(moneySpentForDaysPrior), 5)]
    print(subListMoneySpentPrior)

    sortedInitialSpent = cs.sortListOfNumbers(subListMoneySpentPrior[1])
    initialMedianSpent = sortedInitialSpent[len(sortedInitialSpent) // 2]
    print(initialMedianSpent)

    counter = 0

    for index in range(1, len(subListMoneySpentPrior)):
        sortedInitialSpent = cs.sortListOfNumbers(subListMoneySpentPrior[index])
        initialMedianSpent = sortedInitialSpent[len(sortedInitialSpent) // 2]
        if initialMedianSpent < moneySpentForDaysPrior[index * 5]:
            counter += 1
    return counter


if __name__ == "__main__":
    sys.stdin = open('FraudulentActivityNotifications_input.txt')
    daysNumData, daysPrior = input().strip().split(' ')
    daysNumData, daysPrior = [int(daysNumData), int(daysPrior)]
    moneySpentDaily = list(map(int, input().strip().split(' ')))
    result = activityNotifications(moneySpentDaily, daysPrior)
    print(result)
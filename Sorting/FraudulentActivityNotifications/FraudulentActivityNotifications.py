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
    sortedInitialSpent = cs.sortListOfNumbers(initialMedianSpentList)
    initialMedianSpent = sortedInitialSpent[len(sortedInitialSpent) // 2]



    for index in range(daysPriorIndex, len(moneySpentDaily) - daysPriorIndex):
        moneySpentForDaysPrior = []
        for i in range(0, daysPrior):
            moneySpentForDaysPrior.append(moneySpentDaily[index + i])
        return moneySpentForDaysPrior


if __name__ == "__main__":
    sys.stdin = open('FraudulentActivityNotifications_input.txt')
    daysNumData, daysPrior = input().strip().split(' ')
    daysNumData, daysPrior = [int(daysNumData), int(daysPrior)]
    moneySpentDaily = list(map(int, input().strip().split(' ')))
    result = activityNotifications(moneySpentDaily, daysPrior)
    print(result)
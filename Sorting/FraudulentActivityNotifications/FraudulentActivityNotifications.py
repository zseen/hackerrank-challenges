#!/bin/python3

import sys
from Library.Sorting import CountingSort


def activityNotifications(moneySpentDaily, daysPrior):
    counter = 0

    for index in range(0, len(moneySpentDaily) - daysPrior):
        # print(index / (len(moneySpentDaily) - daysPrior) * 100)
        moneySpentForDaysPrior = []
        for i in range(0, daysPrior):
            moneySpentForDaysPrior.append(moneySpentDaily[index + i])

        sortedDailySpent = CountingSort.sortListOfNumbers(moneySpentForDaysPrior)
        medianSpent = sortedDailySpent[len(sortedDailySpent) // 2]
        if medianSpent * 2 <= moneySpentDaily[index + daysPrior]:
            counter += 1

    return counter


def main():
    sys.stdin = open('FraudulentActivityNotifications_input.txt')
    daysNumData, daysPrior = input().strip().split(' ')
    daysNumData, daysPrior = [int(daysNumData), int(daysPrior)]
    moneySpentDaily = list(map(int, input().strip().split(' ')))
    result = activityNotifications(moneySpentDaily, daysPrior)
    print(result)


if __name__ == "__main__":
    main()

#!/bin/python3

import sys
from Library.Sorting import CountingSort as cs


def activityNotifications(moneySpentDaily, daysPrior):
    counter = -1

    for index in range(0, len(moneySpentDaily) - daysPrior):
        moneySpentForDaysPrior = []
        for i in range(0, daysPrior):
            moneySpentForDaysPrior.append(moneySpentDaily[index + i])
            if len(moneySpentForDaysPrior) == daysPrior:
                sortedDailySpent = cs.sortListOfNumbers(moneySpentForDaysPrior)
                medianSpent = sortedDailySpent[len(sortedDailySpent) // 2]
                if medianSpent < moneySpentDaily[index + 5]:
                    counter += 1

    if counter < 0:
        return counter + 1
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

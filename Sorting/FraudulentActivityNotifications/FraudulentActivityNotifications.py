#!/bin/python3

import sys


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


def getMedian(moneySpentDaily, daysPrior):
    counter = getNumCounter(moneySpentDaily, daysPrior)

    if daysPrior % 2 != 0:
        medianItem = (daysPrior // 2) + 1
        listSum = 0

        for item in counter:
            listSum += item
            if listSum >= medianItem:
                median = medianItem
                return median
    else:
        medianItem1 = daysPrior // 2
        medianItem2 = daysPrior // 2 + 1
        medianItemAv = (medianItem1 + medianItem2) / 2
        listSum = 0
        for item in counter:
            listSum += item
            if listSum >= medianItemAv:
                median = medianItemAv
                return median


def countNotifications(moneySpentDaily, daysPrior):
    notificationCounter = 0

    for index in range(0, len(moneySpentDaily) - daysPrior):
        moneySpentForDaysPrior = []
        for i in range(0, daysPrior):
            moneySpentForDaysPrior.append(moneySpentDaily[index + i])
        median = getMedian(moneySpentForDaysPrior, daysPrior)
        if moneySpentDaily[index + daysPrior] >= median * 2:
            notificationCounter += 1
    return notificationCounter


def main():
    sys.stdin = open('FraudulentActivityNotifications_input.txt')
    daysNumData, daysPrior = input().strip().split(' ')
    daysNumData, daysPrior = [int(daysNumData), int(daysPrior)]
    moneySpentDaily = list(map(int, input().strip().split(' ')))

    notifications = countNotifications(moneySpentDaily, daysPrior)
    print(notifications)


if __name__ == "__main__":
    main()

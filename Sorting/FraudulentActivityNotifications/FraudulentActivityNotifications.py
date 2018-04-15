#!/bin/python3

import sys
import unittest


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


def getMedian(daysPrior, COUNTER):
    counter = COUNTER

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


def countNotifications(COUNTER, moneySpentDaily, daysPrior):
    notificationCounter = 0

    for index in range(0, len(moneySpentDaily) - daysPrior):
        moneySpentForDaysPrior = []
        for i in range(0, daysPrior):
            moneySpentForDaysPrior.append(moneySpentDaily[index + i])
        median = getMedian(daysPrior, COUNTER)
        if moneySpentDaily[index + daysPrior] >= median * 2:
            notificationCounter += 1
    return notificationCounter


def main():
    sys.stdin = open('FraudulentActivityNotifications_input.txt')
    daysNumData, daysPrior = input().strip().split(' ')
    daysNumData, daysPrior = [int(daysNumData), int(daysPrior)]
    moneySpentDaily = list(map(int, input().strip().split(' ')))
    COUNTER = getNumCounter(moneySpentDaily, daysPrior)

    notifications = countNotifications(COUNTER, moneySpentDaily, daysPrior)
    print(notifications)
    #should be 633


if __name__ == "__main__":
    #main()
    unittest.main()


class TestNotificationCount(unittest.TestCase):

    def test_5daysPrior_2notifications(self, COUNTER):
        daysPrior = 5
        moneySpentDaily = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        notifications = countNotifications(COUNTER, moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 2)

    def test_4daysPrior_0notifications(self, COUNTER):
        daysPrior = 4
        moneySpentDaily = [1, 2, 3, 4, 4]
        notifications = countNotifications(COUNTER, moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_3daysPrior_1notification(self, COUNTER):
        daysPrior = 3
        moneySpentDaily = [1, 2, 3, 4, 5]
        notifications = countNotifications(COUNTER, moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def t4(self):
        self.assertTrue(0 == 0)
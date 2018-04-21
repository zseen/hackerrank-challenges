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


def getMedian(daysPrior, counter):

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
        counter = getNumCounter(moneySpentDaily, daysPrior)
        moneySpentForDaysPrior = []
        for i in range(0, daysPrior):
            moneySpentForDaysPrior.append(moneySpentDaily[index + i])
        median = getMedian(daysPrior, counter)
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


class TestNotificationCount(unittest.TestCase):
    def test_moreDaysPriorThanDays_0notifications(self):
        daysPrior = 6
        moneySpentDaily = [1, 2, 3, 4, 5]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_sameMoneySpent_0notifications(self):
        daysPrior = 3
        moneySpentDaily = [2, 2, 2, 2, 2]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_evenDaysPrior_0notifications(self):
        daysPrior = 4
        moneySpentDaily = [1, 2, 3, 4, 4]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_oddDaysPrior_1notifications(self):
        daysPrior = 3
        moneySpentDaily = [1, 2, 3, 4, 5]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def test_evenDaysPriorDifferentElementsInMiddle_1notification(self):
        daysPrior = 4
        moneySpentDaily = [1, 2, 3, 4, 4, 7]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def test_evenDaysPriorSameElementInMiddle_1notification(self):
        daysPrior = 4
        moneySpentDaily = [1, 2, 4, 4, 4, 8]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def test_slightlyLongerArray_2notifications(self):
        daysPrior = 5
        moneySpentDaily = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 2)

    def test_incrementingElements_0notifications(self):
        daysPrior = 3
        moneySpentDaily = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_incrementingElements_1notification(self):
        daysPrior = 3
        moneySpentDaily = [2, 3, 4, 5, 6, 7, 8, 1000, 9, 10, 11, 12, 13]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def test_largeNumbers_0notification(self):
        daysPrior = 2
        moneySpentDaily = [10000, 10001, 15000, 20000, 27000, 39000]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

if __name__ == "__main__":
    #main()
    unittest.main()
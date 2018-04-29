#!/bin/python3

import sys
import unittest


def iterateSubArray(moneySpentDaily, daysPrior):
    for index in range(0, len(moneySpentDaily) - daysPrior - 1):
        currentArray = moneySpentDaily[index : index + daysPrior]
        cnt  = getNumCounter(currentArray, daysPrior)


def getNumCounter(listSpent, priorDays):
    daysPriorSpent = []
    for index in range(0, priorDays):
        daysPriorSpent.append(listSpent[index])

    biggestNum = max(daysPriorSpent)
    smallestNum = min(daysPriorSpent)

    counter = [0] * 200

    for item in daysPriorSpent:
        counter[item] += 1

    return counter

def getMedian(daysPrior, moneySpentDaily):
    counter = getNumCounter(moneySpentDaily, daysPrior)
    median = 0
    medHelp = (len(moneySpentDaily) // 2)

    if len(moneySpentDaily) % 2 != 0:
        medianIndex = medHelp  + 1
        index = 0
        for item in counter:
            index += item
            if index == medianIndex:
                median = counter[index]
                return median
    else:
        medianIndex1 = medHelp
        index = 0
        for item in counter:
            index += item
            if index >= medianIndex1:
                for i in range(medianIndex1, 200 - medianIndex1):
                    if counter[i] > 0:
                        medianIndex2 = counter[i]
                    median = (counter[index] + counter[i]) / 2
                    return median









def countNotifications(moneySpentDaily, daysPrior):
    notificationCounter = 0

    for index in range(0, len(moneySpentDaily) - daysPrior):
        moneySpentForDaysPrior = []
        for i in range(0, daysPrior):
            moneySpentForDaysPrior.append(moneySpentDaily[index + i])
        counter = getNumCounter(daysPrior, moneySpentForDaysPrior)
        median = getMedian(daysPrior, moneySpentDaily)
        if moneySpentDaily[index + daysPrior] >= median * 2:
            notificationCounter += 1
    return notificationCounter


# FOR TESTING ONLY
def getMedianFromSortedArray(sortedDailySpent):
    midIndex = len(sortedDailySpent) // 2
    midElem = sortedDailySpent[midIndex]
    if len(sortedDailySpent) % 2 != 0:
        medianSpent = midElem
    else:
        leftToMidElem = sortedDailySpent[midIndex - 1]
        medianSpent = (midElem + leftToMidElem) / 2
    return medianSpent

def countNotificationsSimple(moneySpentDaily, daysPrior):
    counter = 0

    for index in range(0, len(moneySpentDaily) - daysPrior):
        moneySpentForDaysPrior = []
        for i in range(0, daysPrior):
            moneySpentForDaysPrior.append(moneySpentDaily[index + i])

        sortedDailySpent = sorted(moneySpentForDaysPrior)
        medianSpent = getMedianFromSortedArray(sortedDailySpent)

        if medianSpent * 2 <= moneySpentDaily[index + daysPrior]:
            counter += 1

    return counter

def main():
    sys.stdin = open('FraudulentActivityNotifications_input.txt')
    daysNumData, daysPrior = input().strip().split(' ')
    daysNumData, daysPrior = [int(daysNumData), int(daysPrior)]
    moneySpentDaily = list(map(int, input().strip().split(' ')))

    #notifications = countNotifications(moneySpentDaily, daysPrior)
    #print(notifications)
    cnt = getNumCounter(moneySpentDaily, daysPrior)
    #print(cnt)
    currentArray = iterateSubArray(moneySpentDaily, daysPrior)
    print(currentArray)


class TestNotificationCount(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestNotificationCount, self).__init__(*args, **kwargs)

        self.countNotificationsImpl = countNotifications

    def test_moreDaysPriorThanDays_0notifications(self):
        daysPrior = 6
        moneySpentDaily = [1, 2, 3, 4, 5]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_sameMoneySpent_0notifications(self):
        daysPrior = 3
        moneySpentDaily = [2, 2, 2, 2, 2]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_evenDaysPrior_0notifications(self):
        daysPrior = 4
        moneySpentDaily = [1, 2, 3, 4, 4]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_oddDaysPrior_1notifications(self):
        daysPrior = 3
        moneySpentDaily = [1, 2, 3, 4, 5]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def test_evenDaysPriorDifferentElementsInMiddle_1notification(self):
        daysPrior = 4
        moneySpentDaily = [1, 2, 3, 4, 4, 7]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def test_evenDaysPriorSameElementInMiddle_1notification(self):
        daysPrior = 4
        moneySpentDaily = [1, 2, 4, 4, 4, 8]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def test_slightlyLongerArray_2notifications(self):
        daysPrior = 5
        moneySpentDaily = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 2)

    def test_incrementingElements_0notifications(self):
        daysPrior = 3
        moneySpentDaily = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_incrementingElements_1notification(self):
        daysPrior = 3
        moneySpentDaily = [2, 3, 4, 5, 6, 7, 8, 1000, 9, 10, 11, 12, 13]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def test_largeNumbers_0notification(self):
        daysPrior = 2
        moneySpentDaily = [10000, 10001, 15000, 20000, 27000, 39000]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_median_odd(self):
        

if __name__ == "__main__":
    main()
    #unittest.main()
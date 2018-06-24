#!/bin/python3

import sys
import unittest


MAX_MONEY_SPENT_A_DAY = 200


def getNumCounter(listSpent, priorDays):
    if len(listSpent) < priorDays:
        return 0
    daysPriorSpent = []
    for index in range(0, priorDays):
        daysPriorSpent.append(listSpent[index])

    counter = [0] * (MAX_MONEY_SPENT_A_DAY + 1)

    for item in daysPriorSpent:
        counter[item] += 1

    return counter


def getMedianOdd(counter, numItems):
    medianItem = (numItems // 2)

    medianIndex = medianItem + 1
    index = 0
    for i in range(0, MAX_MONEY_SPENT_A_DAY):
        index += counter[i]
        if index >= medianIndex:
            return i


def getMedianEven(counter, numItems):
    medianItem = (numItems // 2)

    medianSmallerIndex = medianItem
    index = 0
    for i in range(0, MAX_MONEY_SPENT_A_DAY):
        index += counter[i]
        if index >= medianSmallerIndex:
            median1 = i
            if index >= medianSmallerIndex + 1:
                return i
            else:
                for idx in range(i + 1, MAX_MONEY_SPENT_A_DAY - i):
                    if counter[idx] > 0:
                        median2 = idx
                        median = (median1 + median2) / 2
                        return median


def getMedian(counter, numItems):
    if numItems % 2 != 0:
        median = getMedianOdd(counter, numItems)

    else:
        median = getMedianEven(counter, numItems)

    return median


def countNotifications(moneySpentDaily, daysPrior):
    notificationCounter = 0
    moneySpentForDaysPrior = moneySpentDaily[0: daysPrior]
    counter = getNumCounter(moneySpentForDaysPrior, daysPrior)

    for index in range(0, len(moneySpentDaily) - daysPrior):
        median = getMedian(counter, daysPrior)
        if moneySpentDaily[index + daysPrior] >= median * 2:
            notificationCounter += 1

        if index < len(moneySpentDaily) - daysPrior - 1:
            counter[moneySpentDaily[index]] -= 1
            counter[moneySpentDaily[index + daysPrior]] += 1

    return notificationCounter


def main():
    sys.stdin = open('FraudulentActivityNotifications_input.txt')
    daysNumData, daysPrior = input().strip().split(' ')
    daysNumData, daysPrior = [int(daysNumData), int(daysPrior)]
    moneySpentDaily = list(map(int, input().strip().split(' ')))
    if daysNumData < daysPrior:
        return 0

    notifications = countNotifications(moneySpentDaily, daysPrior)
    print(notifications)


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

    def wrongTestcase_tooLargeNumber_test_incrementingElements_1notification(self):
        daysPrior = 3
        moneySpentDaily = [2, 3, 4, 5, 6, 7, 8, 1000, 9, 10, 11, 12, 13]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def wrongTestcase_tooLargeNumbers_test_largeNumbers_0notification(self):
        daysPrior = 2
        moneySpentDaily = [10000, 10001, 15000, 20000, 27000, 39000]
        notifications = self.countNotificationsImpl(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_median_odd(self):
        daysPrior = 3
        moneySpentDaily = [20, 40, 30]
        counter = getNumCounter(moneySpentDaily, daysPrior)
        median = getMedian(counter, daysPrior)
        print(median)
        self.assertTrue(median == 30)

    def test_median_odd_longerArray(self):
        daysPrior = 9
        moneySpentDaily = [20, 78, 1, 1, 1, 20, 40, 30, 199]
        counter = getNumCounter(moneySpentDaily, daysPrior)
        median = getMedian(counter, daysPrior)
        print(median)
        self.assertTrue(median == 20)

    def test_median_odd_sameNumbers(self):
        daysPrior = 5
        moneySpentDaily = [45, 45, 45, 45, 45]
        counter = getNumCounter(moneySpentDaily, daysPrior)
        median = getMedian(counter, daysPrior)
        print(median)
        self.assertTrue(median == 45)

    def test_median_odd_onlyBigNumbers(self):
        daysPrior = 5
        moneySpentDaily = [200, 198, 197, 199, 196]
        counter = getNumCounter(moneySpentDaily, daysPrior)
        median = getMedian(counter, daysPrior)
        print(median)
        self.assertTrue(median == 198)

    def test_median_even_2DifferentMedNums_medFraction(self):
        daysPrior = 4
        moneySpentDaily = [2, 3, 3, 2]
        counter = getNumCounter(moneySpentDaily, daysPrior)
        median = getMedian(counter, daysPrior)
        print(median)
        self.assertTrue(median == 2.5)

    def test_median_even_biggerRangeNums2DiffMedNums_medWhole(self):
        daysPrior = 6
        moneySpentDaily = [4, 20, 62, 3, 100, 0]
        counter = getNumCounter(moneySpentDaily, daysPrior)
        median = getMedian(counter, daysPrior)
        print(median)
        self.assertTrue(median == 12)

    def test_median_even_sameMedianNums(self):
        daysPrior = 6
        moneySpentDaily = [20, 20, 62, 3, 100, 0]
        counter = getNumCounter(moneySpentDaily, daysPrior)
        median = getMedian(counter, daysPrior)
        print(median)
        self.assertTrue(median == 20)


if __name__ == "__main__":
    main()
    #unittest.main()
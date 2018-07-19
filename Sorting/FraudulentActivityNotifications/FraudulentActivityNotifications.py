#!/bin/python3

import sys
import unittest


MAX_MONEY_SPENT_A_DAY = 200


def getNumCounter(numbersList, maxNumber):
    daysPriorSpent = []
    for index in range(0, len(numbersList)):
        daysPriorSpent.append(numbersList[index])

    counter = [0] * (maxNumber + 1)

    for item in daysPriorSpent:
        counter[item] += 1

    return counter


def getMedianOdd(counter, numItems):
    medianItem = (numItems // 2)
    medianIndex = medianItem + 1
    numbersSeenTotal = 0
    for i in range(0, len(counter)):
        numbersSeenTotal += counter[i]
        if numbersSeenTotal >= medianIndex:
            return i


def findNextNonZeroIndex(numsList, startFrom):
    try:
        for index in range(startFrom, len(numsList) + 1):
            if numsList[index] > 0:
                return index
    except IndexError:
        print("No non-zero element has been found")


def getMedianEven(counter, numItems):
    medianItem = (numItems // 2)
    medianSmallerIndex = medianItem
    numbersSeenTotal = 0
    for firstIndex in range(0, len(counter)):
        numbersSeenTotal += counter[firstIndex]
        if numbersSeenTotal >= medianSmallerIndex:
            medianFirstItem = firstIndex
            if numbersSeenTotal >= medianSmallerIndex + 1:
                return medianFirstItem
            else:
                medianSecondItem = findNextNonZeroIndex(counter, firstIndex + 1)
                return (medianFirstItem + medianSecondItem) / 2


def getMedian(counter, numItems):
    if numItems % 2 != 0:
        return getMedianOdd(counter, numItems)
    else:
        return getMedianEven(counter, numItems)


def countNotifications(moneySpentDaily, daysPrior):
    notificationCounter = 0
    moneySpentForDaysPrior = moneySpentDaily[0: daysPrior]
    counter = getNumCounter(moneySpentForDaysPrior, MAX_MONEY_SPENT_A_DAY)

    for index in range(daysPrior, len(moneySpentDaily)):
        median = getMedian(counter, daysPrior)
        if moneySpentDaily[index] >= median * 2:
            notificationCounter += 1

        if index < len(moneySpentDaily) - 1:
            counter[moneySpentDaily[index - daysPrior]] -= 1
            counter[moneySpentDaily[index]] += 1

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

    def test_countNotifications_moreDaysPriorThanDays_0notifications(self):
        daysPrior = 6
        moneySpentDaily = [1, 2, 3, 4, 5]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_countNotifications_sameMoneySpent_0notifications(self):
        daysPrior = 3
        moneySpentDaily = [2, 2, 2, 2, 2]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_countNotifications_evenDaysPrior_0notifications(self):
        daysPrior = 4
        moneySpentDaily = [1, 2, 3, 4, 4]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_countNotifications_oddDaysPrior_1notifications(self):
        daysPrior = 3
        moneySpentDaily = [1, 2, 3, 4, 5]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def test_countNotifications_evenDaysPriorDifferentElementsInMiddle_1notification(self):
        daysPrior = 4
        moneySpentDaily = [1, 2, 3, 4, 4, 7]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def test_countNotifications_evenDaysPriorSameElementInMiddle_1notification(self):
        daysPrior = 4
        moneySpentDaily = [1, 2, 4, 4, 4, 8]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 1)

    def test_countNotifications_slightlyLongerArray_2notifications(self):
        daysPrior = 5
        moneySpentDaily = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 2)

    def test_countNotifications_incrementingElements_0notifications(self):
        daysPrior = 3
        moneySpentDaily = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        notifications = countNotifications(moneySpentDaily, daysPrior)
        self.assertTrue(notifications == 0)

    def test_countNotifications_tooLargeNumber_raisesIndexError(self):
        try:
            daysPrior = 3
            moneySpentDaily = [2, 3, 4, 5, 6, 7, 8, 1000, 9, 10, 11, 12, 13]
            notifications = countNotifications(moneySpentDaily, daysPrior)
            self.assertTrue(notifications == 1)
        except IndexError:
            self.assertRaises(IndexError)

    def test_countNotifications_tooLargeNumbers_raisesIndexError(self):
        try:
            daysPrior = 2
            moneySpentDaily = [10000, 10001, 15000, 20000, 27000, 39000]
            notifications = countNotifications(moneySpentDaily, daysPrior)
            self.assertTrue(notifications == 0)
        except IndexError:
            self.assertRaises(IndexError)

    def test_getMedian_oddNumberElements_shortArray(self):
        daysPrior = 3
        moneySpentDaily = [20, 40, 30]
        counter = getNumCounter(moneySpentDaily, MAX_MONEY_SPENT_A_DAY)
        median = getMedian(counter, daysPrior)
        self.assertTrue(median == 30)

    def test_getMedian_oddNumberElements_longerArray(self):
        daysPrior = 9
        moneySpentDaily = [20, 78, 1, 1, 1, 20, 40, 30, 199]
        counter = getNumCounter(moneySpentDaily, MAX_MONEY_SPENT_A_DAY)
        median = getMedian(counter, daysPrior)
        self.assertTrue(median == 20)

    def test_getMedian_oddNumberElements_sameNumbers(self):
        daysPrior = 5
        moneySpentDaily = [45, 45, 45, 45, 45]
        counter = getNumCounter(moneySpentDaily, MAX_MONEY_SPENT_A_DAY)
        median = getMedian(counter, daysPrior)
        self.assertTrue(median == 45)

    def test_getMedian_oddNumberElements_onlyBigNumbers(self):
        daysPrior = 5
        moneySpentDaily = [200, 198, 197, 199, 196]
        counter = getNumCounter(moneySpentDaily, MAX_MONEY_SPENT_A_DAY)
        median = getMedian(counter, daysPrior)
        self.assertTrue(median == 198)

    def test_getMedian_evenNumberElements_2DifferentMedNums_medFraction(self):
        daysPrior = 4
        moneySpentDaily = [2, 3, 3, 2]
        counter = getNumCounter(moneySpentDaily, MAX_MONEY_SPENT_A_DAY)
        median = getMedian(counter, daysPrior)
        self.assertTrue(median == 2.5)

    def test_getMedian_evenNumberElements_biggerRangeNums2DiffMedNums_medWhole(self):
        daysPrior = 6
        moneySpentDaily = [4, 20, 62, 3, 100, 0]
        counter = getNumCounter(moneySpentDaily, MAX_MONEY_SPENT_A_DAY)
        median = getMedian(counter, daysPrior)
        self.assertTrue(median == 12)

    def test_getMedian_evenNumberElements_sameMedianNums(self):
        daysPrior = 6
        moneySpentDaily = [20, 20, 62, 3, 100, 0]
        counter = getNumCounter(moneySpentDaily, MAX_MONEY_SPENT_A_DAY)
        median = getMedian(counter, daysPrior)
        self.assertTrue(median == 20)

    def test_getMedian_evenNumberElements_secondMedianItemIsMaxValue(self):
        daysPrior = 6
        moneySpentDaily = [100, 100, 100, 200, 200, 200]
        counter = getNumCounter(moneySpentDaily, MAX_MONEY_SPENT_A_DAY)
        median = getMedian(counter, daysPrior)
        self.assertTrue(median == 150)


if __name__ == "__main__":
    main()
    #unittest.main()
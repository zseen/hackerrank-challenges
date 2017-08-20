#!/bin/python3

import sys

def isYearLeapYear(year):
    if year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
    elif year <1918:
        if year % 4 == 0:
            return True
    return False

# def returnTheDate(year):
#     sumOfDays = 0
#     lp = monthsIfLeap()
#
#     if sumOfDays + value >= 256:
#         x = [256 - sumOfDays, key]
#         monthNum = monthsAsNumbers[sumOfDays // 30]
#         return str(x[0]) + "." + str(monthNum) + "." + str(year)

def monthsIfLeap():
    monthsIfLeapYear = [("January",31), ("February", 29), ("March", 31), ("April", 30), ("May", 31), ("June", 30), ("July", 31),
    ("August", 31), ("September", 30), ("October", 31), ("November", 30), ("December", 31)]
    return monthsIfLeapYear


def monthsIfNotLeap():
    monthsIfNotLeapYear = [("January",31), ("February", 28), ("March", 31), ("April", 30), ("May", 31), ("June", 30), ("July", 31),
    ("August", 31), ("September", 30), ("October", 31), ("November", 30), ("December", 31)]
    return monthsIfNotLeapYear


def solve(year):
    lp = monthsIfLeap()
    nlp = monthsIfNotLeap()
    monthsAsNumbers = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

    if year == 1918:
        sumOfDays = -13
        for item in range(0,len(nlp)):
            if sumOfDays + nlp[item][1] >= 256:
                x = [256 - sumOfDays, nlp[item][0]]
                monthNum = monthsAsNumbers[item]
                return str(x[0]) + "." + str(monthNum) + "." + str(year)
            sumOfDays += nlp[item][1]

    sumOfDays = 0
    if isYearLeapYear(year) is True:
        for item in range(0,len(lp)):
            if sumOfDays + lp[item][1] >= 256:
                x = [256 - sumOfDays, lp[item][0]]
                monthNum = monthsAsNumbers[item]
                return str(x[0]) + "." + str(monthNum) + "." + str(year)
            sumOfDays += lp[item][1]
    else:
        for item in range(0,len(nlp)):
            if sumOfDays + nlp[item][1] >= 256:
                x = [256 - sumOfDays, nlp[item][0]]
                monthNum = monthsAsNumbers[item]
                return str(x[0]) + "." + str(monthNum) + "." + str(year)
            sumOfDays += nlp[item][1]




sys.stdin = open('dayOfTheProgrammer_input.txt')
year = int(input().strip())
result = solve(year)
print(result)



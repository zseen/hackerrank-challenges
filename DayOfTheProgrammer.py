#!/bin/python3

import sys

dayOfTheProgrammer = 256
yearOfCalendarChange = 1918
differenceIn1918 = -13
sumOfDays = 0


def isYearLeapYear(year):
    if year > yearOfCalendarChange:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
    elif year < yearOfCalendarChange:
        if year % 4 == 0:
            return True
    return False


def monthsIfLeap():
    monthsIfLeapYear = [("January", 31), ("February", 29), ("March", 31), ("April", 30), ("May", 31), ("June", 30),
                        ("July", 31), ("August", 31), ("September", 30), ("October", 31),
                        ("November", 30), ("December", 31)]
    return monthsIfLeapYear


def monthsIfNotLeap():
    monthsIfNotLeapYear = [("January", 31), ("February", 28), ("March", 31), ("April", 30), ("May", 31), ("June", 30),
                           ("July", 31), ("August", 31), ("September", 30), ("October", 31),
                           ("November", 30), ("December", 31)]
    return monthsIfNotLeapYear


def calculateTheDayIfNotLeap(nlp, sumOfDays, year):
    for item in range(0, len(nlp)):
        if sumOfDays + nlp[item][1] >= dayOfTheProgrammer:
            day = dayOfTheProgrammer - sumOfDays
            return str(day) + "." + str(item + 1).zfill(2) + "." + str(year)
        sumOfDays += nlp[item][1]


def calculateTheDayIfLeap(lp, sumOfDays, year):
    for item in range(0, len(lp)):
        if sumOfDays + lp[item][1] >= dayOfTheProgrammer:
            day = dayOfTheProgrammer - sumOfDays
            return str(day) + "." + str(item + 1).zfill(2) + "." + str(year)
        sumOfDays += lp[item][1]


def solve(year, sumOfDays):
    lp = monthsIfLeap()
    nlp = monthsIfNotLeap()

    if year == yearOfCalendarChange:
        sumOfDays += differenceIn1918
        return calculateTheDayIfNotLeap(nlp, sumOfDays, year)
    elif isYearLeapYear(year) is True:
        return calculateTheDayIfLeap(lp, sumOfDays, year)
    else:
        return calculateTheDayIfNotLeap(nlp, sumOfDays, year)


def main():
    sys.stdin = open('dayOfTheProgrammer_input.txt')
    year = int(input().strip())
    result = solve(year, sumOfDays)
    print(result)

if __name__ == "__main__":
    main()





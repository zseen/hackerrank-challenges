#!/bin/python3

import sys

dayOfTheProgrammer = 256
yearOfCalendarChange = 1918
differenceIn1918 = -13


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


def calculateTheDay(listOfMonths, sumOfDays, year):
    for item in range(0, len(listOfMonths)):
        if sumOfDays + listOfMonths[item][1] >= dayOfTheProgrammer:
            day = dayOfTheProgrammer - sumOfDays
            return str(day) + "." + str(item + 1).zfill(2) + "." + str(year)
        sumOfDays += listOfMonths[item][1]


def solve(year):
    lp = monthsIfLeap()
    nlp = monthsIfNotLeap()

    sumOfDays = 0

    if year == yearOfCalendarChange:
        sumOfDays += differenceIn1918
        return calculateTheDay(nlp, sumOfDays, year)
    elif isYearLeapYear(year) is True:
        return calculateTheDay(lp, sumOfDays, year)
    else:
        return calculateTheDay(nlp, sumOfDays, year)


def main():
    sys.stdin = open('DayOfTheProgrammer_input.txt')
    year = int(input().strip())
    result = solve(year)
    print(result)

if __name__ == "__main__":
    main()





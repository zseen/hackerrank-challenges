import math
import os
import random
import re
import sys


def libraryFine(day1, month1, year1, day2, month2, year2):
    fine = 0
    if year1 > year2:
        fine = 10000

    elif year1 == year2:
        if month1 > month2:
            fine = (month1 - month2) * 500
        elif month1 == month2 and day1 > day2:
            fine = (day1 - day2) * 15

    return fine


def main():
    sys.stdin = open('LibraryFineInput.txt')

    d1M1Y1 = input().split()
    day1 = int(d1M1Y1[0])
    month1 = int(d1M1Y1[1])
    year1 = int(d1M1Y1[2])
    d2M2Y2 = input().split()
    day2 = int(d2M2Y2[0])
    month2 = int(d2M2Y2[1])
    year2 = int(d2M2Y2[2])
    result = libraryFine(day1, month1, year1, day2, month2, year2)

    print(result)

if __name__ == "__main__":
    main()

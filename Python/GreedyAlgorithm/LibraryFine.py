import math
import os
import random
import re
import sys


def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    if y1 > y2:
        fine = 10000

    elif y1 == y2:
        if m1 > m2:
            fine = (m1 - m2) * 500
        elif m1 == m2 and d1 > d2:
            fine = (d1 - d2) * 15

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

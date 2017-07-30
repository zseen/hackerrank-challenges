#!/bin/python3

import sys


def solve(grades):
    roundedGrades = []
    for grade in grades:
        if grade < 38 or grade % 5 == 0:
            roundedGrades.append(grade)
        elif grade % 5 != 0:
            if (grade + 2) % 5 == 0:
                roundedGrades.append(grade + 2)
            elif (grade + 1) % 5 == 0:
                roundedGrades.append(grade + 1)
            else:
                roundedGrades.append(grade)
    return roundedGrades


def main():
    sys.stdin = open('gradingstudents_input.txt')
    n = int(input().strip())
    grades = []
    grades_i = 0
    for grades_i in range(n):
        grades_t = int(input().strip())
        grades.append(grades_t)
    result = solve(grades)
    print("\n".join(map(str, result)))

if __name__ == "__main__":
    main()


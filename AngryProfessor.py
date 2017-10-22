#!/bin/python3

import sys


def arriveInTime(arrivalTime):
    studentInTime = 0
    for item in arrivalTime:
        if item <= 0:
            studentInTime += 1
    return studentInTime


def getCancelled(studentsToBePresent, arrivalTime):
    inTime = arriveInTime(arrivalTime)

    if inTime >= studentsToBePresent:
        return False
    return True


def main():
    sys.stdin = open('angryProfessor_input.txt')
    t = int(input().strip())
    for a0 in range(t):
        numberOfStudentsAltogether, studentsToBePresent = input().strip().split(' ')
        numberOfStudentsAltogether, studentsToBePresent = [int(numberOfStudentsAltogether), int(studentsToBePresent)]
        arrivalTime = [int(a_temp) for a_temp in input().strip().split(' ')]
        cancelled = getCancelled(studentsToBePresent, arrivalTime)
        if cancelled is True:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()





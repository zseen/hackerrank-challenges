#!/bin/python3
import unittest

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


class TestWinChecking(unittest.TestCase):
    def test_getCancelled_6studentsToBePresent_47inTime_notcancelled(self):
        sys.stdin = open('angryProfessor_unittest1_input.txt')
        numberOfStudentsAltogether, studentsToBePresent = input().strip().split(' ')
        numberOfStudentsAltogether, studentsToBePresent = [int(numberOfStudentsAltogether), int(studentsToBePresent)]
        arrivalTime = [int(a_temp) for a_temp in input().strip().split(' ')]
        cancelled = getCancelled(studentsToBePresent, arrivalTime)
        self.assertTrue(cancelled is False)

    def test_getCancelled_77studentsToBePresent_45inTime_cancelled(self):
        sys.stdin = open('angryProfessor_unittest2_input.txt')
        numberOfStudentsAltogether, studentsToBePresent = input().strip().split(' ')
        numberOfStudentsAltogether, studentsToBePresent = [int(numberOfStudentsAltogether), int(studentsToBePresent)]
        arrivalTime = [int(a_temp) for a_temp in input().strip().split(' ')]
        cancelled = getCancelled(studentsToBePresent, arrivalTime)
        self.assertTrue(cancelled is True)

    def test_getCancelled_190studentsToBePresent_445inTime_notCancelled(self):
        sys.stdin = open('angryProfessor_unittest3_input.txt')
        numberOfStudentsAltogether, studentsToBePresent = input().strip().split(' ')
        numberOfStudentsAltogether, studentsToBePresent = [int(numberOfStudentsAltogether), int(studentsToBePresent)]
        arrivalTime = [int(a_temp) for a_temp in input().strip().split(' ')]
        x = 0
        for item in arrivalTime:
            if item <= 0:
                x +=1
        print(x)
        cancelled = getCancelled(studentsToBePresent, arrivalTime)
        self.assertTrue(cancelled is False)

if __name__ == "__main__":
    unittest.main()
    #main()




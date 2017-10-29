#!/bin/python3
import unittest

import sys


def numArrivedInTime(arrivalTimes):
    numStudentsInTime = 0
    for item in arrivalTimes:
        if item <= 0:
            numStudentsInTime += 1
    return numStudentsInTime


def isCancelled(studentsToBePresent, arrivalTimes):
    inTime = numArrivedInTime(arrivalTimes)

    if inTime >= studentsToBePresent:
        return False
    return True


def getHelpWithInput():
    numberOfStudentsAltogether, studentsToBePresent = input().strip().split(' ')
    numberOfStudentsAltogether, studentsToBePresent = [int(numberOfStudentsAltogether), int(studentsToBePresent)]
    arrivalTimes = [int(a_temp) for a_temp in input().strip().split(' ')]
    cancelled = isCancelled(studentsToBePresent, arrivalTimes)
    return cancelled


def main():
    sys.stdin = open('angryProfessor_input.txt')
    t = int(input().strip())
    for a0 in range(t):
        cancelled = getHelpWithInput()
        if cancelled is True:
            print("YES")
        else:
            print("NO")


class TestWinChecking(unittest.TestCase):
    def test_isCancelled_6studentsToBePresent_47inTime_notCancelled(self):
        sys.stdin = open('angryProfessor_unittest1_input.txt')
        cancelled = getHelpWithInput()
        self.assertTrue(cancelled is False)

    def test_isCancelled_77studentsToBePresent_45inTime_cancelled(self):
        sys.stdin = open('angryProfessor_unittest2_input.txt')
        cancelled = getHelpWithInput()
        self.assertTrue(cancelled is True)

    def test_isCancelled_190studentsToBePresent_445inTime_notCancelled(self):
        sys.stdin = open('angryProfessor_unittest3_input.txt')
        cancelled = getHelpWithInput()
        self.assertTrue(cancelled is False)

    def test_isCancelled_1studentsToBePresent_0inTime_Cancelled(self):
        sys.stdin = open('angryProfessor_unittest4_input.txt')
        cancelled = getHelpWithInput()
        self.assertTrue(cancelled is True)

    def test_isCancelled_2studentsToBePresent_2inTime_notCancelled(self):
        sys.stdin = open('angryProfessor_unittest5_input.txt')
        cancelled = getHelpWithInput()
        self.assertTrue(cancelled is False)


if __name__ == "__main__":
    unittest.main()
    #main()




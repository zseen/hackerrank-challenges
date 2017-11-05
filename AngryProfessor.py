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


def determineIfCancelledFromStream(streamFunc):
    numberOfStudentsAltogether, studentsToBePresent = streamFunc().strip().split(' ')
    numberOfStudentsAltogether, studentsToBePresent = [int(numberOfStudentsAltogether), int(studentsToBePresent)]
    arrivalTimes = [int(a_temp) for a_temp in streamFunc().strip().split(' ')]
    cancelled = isCancelled(studentsToBePresent, arrivalTimes)
    return cancelled


def main():
    sys.stdin = open('angryProfessor_input.txt')
    t = int(input().strip())
    for a0 in range(t):
        cancelled = determineIfCancelledFromStream(input)
        if cancelled is True:
            print("YES")
        else:
            print("NO")

# rename unit test files
# use new signature for determineIfCancelledFromStream
# write a unit test for isCancelled
# correct unit test names


class TestWinChecking(unittest.TestCase):
    def test_determineIfCancelled_6studentsToBePresent_47inTime_notCancelled(self):
        f = open('angryProfessor_test_determineIfCancelled_6studentsToBePresent_47inTime_notCancelled.txt')
        cancelled = determineIfCancelledFromStream(f.readline)
        self.assertTrue(cancelled is False)

    def test_determineIfCancelled_77studentsToBePresent_45inTime_cancelled(self):
        f = open('angryProfessor_test_determineIfCancelled_77studentsToBePresent_45inTime_cancelled.txt')
        cancelled = determineIfCancelledFromStream(f.readline)
        self.assertTrue(cancelled is True)

    def test_determineIfCancelled_190studentsToBePresent_445inTime_notCancelled(self):
        f = open('angryProfessor_test_determineIfCancelled_190studentsToBePresent_445inTime_notCancelled.txt')
        cancelled = determineIfCancelledFromStream(f.readline)
        self.assertTrue(cancelled is False)

    def test_determineIfCancelled_1studentsToBePresent_0inTime_Cancelled(self):
        f = open('angryProfessor_test_determineIfCancelled_1studentsToBePresent_0inTime_Cancelled.txt')
        cancelled = determineIfCancelledFromStream(f.readline)
        self.assertTrue(cancelled is True)

    def test_determineIfCancelled_2studentsToBePresent_2inTime_notCancelled(self):
        f = open('angryProfessor_test_determineIfCancelled_2studentsToBePresent_2inTime_notCancelled.txt')
        cancelled = determineIfCancelledFromStream(f.readline)
        self.assertTrue(cancelled is False)

    def test_isCancelled(self):
        cancelled = isCancelled(3, [0, 2, -3, 5, -4])
        self.assertTrue(cancelled is False)


if __name__ == "__main__":
    unittest.main()
    #main()




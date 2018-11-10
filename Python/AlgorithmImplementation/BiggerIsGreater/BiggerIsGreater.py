#!/bin/python3

import math
import os
import random
import re
import sys
import unittest


def getNextBiggerPermutation(word):
    wordCharsList = list(word)

    for i in range(len(wordCharsList) - 2, -1, -1):
        if wordCharsList[i] < wordCharsList[i + 1]:
            for j in range(len(wordCharsList) - 1, i - 1, -1):
                if wordCharsList[j] > wordCharsList[i]:
                    wordCharsList[i], wordCharsList[j] = wordCharsList[j], wordCharsList[i]
                    wordCharsList[i + 1:] = reversed(wordCharsList[i + 1:])
                    return "".join(wordCharsList)
    return "no answer"



def main():
    sys.stdin = open("BiggerIsGreater_input.txt")

    T = int(input())

    for T_itr in range(T):
        word = input()
        result = getNextBiggerPermutation(word)
        print(result)


class TestgetNextBiggerPermutation(unittest.TestCase):

    def test_getNextBiggerPermutation_lastTwoCharsSwap(self):
        word = "lmno"
        result = getNextBiggerPermutation(word)
        self.assertTrue(result == "lmon")

    def test_getNextBiggerPermutation_twoCharsLengthWord_swapChars(self):
        word = "ab"
        result = getNextBiggerPermutation(word)
        self.assertTrue(result == "ba")

    def test_getNextBiggerPermutation_allSameChars_noSolution(self):
        word = "bbb"
        result = getNextBiggerPermutation(word)
        self.assertTrue(result == "no answer")

    def test_getNextBiggerPermutation_currentIsBiggest_noSolution(self):
        word = "dcba"
        result = getNextBiggerPermutation(word)
        self.assertTrue(result == "no answer")

    def test_getNextBiggerPermutation_lastAndThirdLastCharsSwap(self):
        word = "abdc"
        result = getNextBiggerPermutation(word)
        self.assertTrue(result == "acbd")

    def test_getNextBiggerPermutation_firstAndSecondLastCharsSwapped(self):
        word = "dkhc"
        result = getNextBiggerPermutation(word)
        self.assertTrue(result == "hcdk")


if __name__ == '__main__':
    main()
    #unittest.main()


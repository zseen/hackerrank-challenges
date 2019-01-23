#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def createSubStringsList(string):
    subStringsList = []
    for i in range(0, len(string) ):
        for j in range(i, len(string) ):
            subStringsList.append(''.join(sorted(string[i:j + 1])))
    return sorted(subStringsList)

def getCharCountInStringsList(s):
    charCountList = []
    st = createSubStringsList(s)
    for sbstr in st:
        c = Counter(sbstr)
        charCountList.append(c)
    return charCountList

def getPatternCode(string):
    countersList = getCharCountInStringsList(string)
    #print(len(countersList))
    pass





def sherlockAndAnagrams(string):
    substrrlist = createSubStringsList(string)

    anagramCounter = 0

    c = Counter(substrrlist)
    print(c)

    for key, value in c.items():
        if c[key] > 1:
            anagramCounter += c[key]
    return anagramCounter  / 2

    #return getPatternCode(string)


if __name__ == '__main__':
    sys.stdin = open("SherlockAndAnagrams_input.txt")

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)

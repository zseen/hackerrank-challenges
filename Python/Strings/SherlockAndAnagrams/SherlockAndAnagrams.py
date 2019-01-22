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
    for i in range(0, len(string)):
        for j in range(i, len(string)):
            subStringsList.append(string[i:j + 1])
    return subStringsList

def getCharCountInString(s):
    st = createSubStringsList(s)
    for sbstr in st:
        c = Counter(sbstr)
        print(c)

def sherlockAndAnagrams(string):

    return getCharCountInString(string)


if __name__ == '__main__':
    sys.stdin = open("SherlockAndAnagrams_input.txt")

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)

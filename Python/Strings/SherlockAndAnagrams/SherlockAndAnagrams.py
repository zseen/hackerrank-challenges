#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(string):
    subStringsDict = {}
    count = 0

    for i in range(0, len(string)):
        for j in range(i + 1, len(string) + 1):
            currentSortedSubString = ''.join(sorted(string[i:j]))
            if currentSortedSubString in subStringsDict:
                count += subStringsDict[currentSortedSubString]
                subStringsDict[currentSortedSubString] += 1

            else:
                subStringsDict[currentSortedSubString] = 1

    return count


if __name__ == '__main__':
    sys.stdin = open("SherlockAndAnagrams_input.txt")

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)

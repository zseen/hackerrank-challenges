#!/bin/python3

import sys

# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(string):
    subStringsDict = {}
    anagramPairsCounter = 0

    for i in range(0, len(string)):
        for j in range(i, len(string)):
            currentSortedSubString = ''.join(sorted(string[i:j + 1]))
            if currentSortedSubString in subStringsDict:
                anagramPairsCounter += subStringsDict[currentSortedSubString]
                subStringsDict[currentSortedSubString] += 1
            else:
                subStringsDict[currentSortedSubString] = 1

    return anagramPairsCounter


if __name__ == '__main__':
    sys.stdin = open("SherlockAndAnagrams_input.txt")
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        print(result)

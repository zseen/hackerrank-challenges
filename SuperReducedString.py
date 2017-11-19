#!/bin/python3

import sys

def super_reduced_string(s):
    charList = list(s)
    for i in range(0, len(charList) - 1):
        if charList[i] == charList[i + 1]:
            charList.pop(i)
            charList.pop(i)
    return s


sys.stdin = open('superReducedString_input.txt')
string = input().strip()
result = super_reduced_string(string)
print(result)

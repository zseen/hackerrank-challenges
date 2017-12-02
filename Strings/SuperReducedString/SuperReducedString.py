#!/bin/python3

import sys


def super_reduced_string(s):
    charList = list(s)
    chIndex = 0
    while chIndex < len(charList) - 1:
        if charList[chIndex] == charList[chIndex + 1]:
            del charList[chIndex]
            del charList[chIndex]
            if chIndex > 0:
                chIndex -= 1
            if len(charList) == 0:
                return None
        else:
            chIndex += 1
    return ''.join(charList)


def main():
    sys.stdin = open('SuperReducedString_input.txt')
    string = input().strip()
    result = super_reduced_string(string)
    if result is None:
        print("Empty String")
    else:
        print(result)

if __name__ == "__main__":
    main()


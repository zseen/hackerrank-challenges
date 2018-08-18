#!/bin/python3

import sys


def getWordCount(camelWord):
    counter = 1
    for char in camelWord:
        if char.isupper() is True:
            counter += 1
    return counter


def main():
    sys.stdin = open('CamelCase_input.txt')
    s = input().strip()
    cnt = getWordCount(s)
    print(cnt)

if __name__ == "__main__":
    main()



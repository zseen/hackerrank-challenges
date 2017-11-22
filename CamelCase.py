#!/bin/python3

import sys


def wordCounter(camelWord):
    counter = 1
    for char in camelWord:
        if char.isupper() is True:
            counter += 1
    return counter


def main():
    sys.stdin = open('camelCase_input.txt')
    s = input().strip()
    cnt = wordCounter(s)
    print(cnt)

if __name__ == "__main__":
    main()



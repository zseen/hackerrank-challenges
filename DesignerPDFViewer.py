#!/bin/python3

import sys
import string


def getArea(word, heightOfLetters):
    alphabet = list(string.ascii_lowercase)
    letterHeightDict = dict(zip(alphabet, heightOfLetters))
    biggestLetter = 0
    wordList = list(word)

    for key, value in letterHeightDict.items():
        if key in wordList:
            if value > biggestLetter:
                biggestLetter = value

    colouredArea = biggestLetter * len(wordList)
    return colouredArea


def main():
    sys.stdin = open('designerPDFViewer_input.txt')
    heightOfLetters = list(map(int, input().strip().split(' ')))
    word = input().strip()
    x = getArea(word, heightOfLetters)
    print(x)


if __name__ == "__main__":
    main()

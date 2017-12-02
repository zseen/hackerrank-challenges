#!/bin/python3

import sys
import string


def getArea(word, heightOfLetters):
    alphabet = list(string.ascii_lowercase)
    letterHeightDict = dict(zip(alphabet, heightOfLetters))
    maxLetterHeight = 0
    wordList = list(word)

    for char in wordList:
        letterHeight = letterHeightDict[char]
        if letterHeight > maxLetterHeight:
            maxLetterHeight = letterHeight

    colouredArea = maxLetterHeight * len(wordList)
    return colouredArea


def main():
    sys.stdin = open('DesignerPDFViewer_input.txt')
    heightOfLetters = list(map(int, input().strip().split(' ')))
    word = input().strip()
    x = getArea(word, heightOfLetters)
    print(x)


if __name__ == "__main__":
    main()

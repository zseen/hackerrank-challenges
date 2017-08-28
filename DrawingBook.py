#!/bin/python3

import sys


def generateBookPages(howManyPages):
    pageList = []
    for item in range(0, howManyPages+1):
        pageList.append(item)
    return pageList


def bookLayout(fromEnd, numberOfPages):
    page = generateBookPages(numberOfPages)

    if len(page) % 2 != 0:
        page.append(0)

    if fromEnd is True:
        page = page[::-1]

    return [page[i: i + 2] for i in range(0, len(page), 2)]


def turnPage(chunks, pageNeeded):
    countFromEnd = 0
    for item in chunks:
        if item[0] == pageNeeded or item[1] == pageNeeded:
            return countFromEnd
        countFromEnd += 1


def solve(pageNeeded, numberOfPages):
    chunksFromBeginning = bookLayout(False, numberOfPages)
    turnBegin = turnPage(chunksFromBeginning, pageNeeded)
    chunksFromEnd = bookLayout(True, numberOfPages)
    turnEnd = turnPage(chunksFromEnd, pageNeeded)

    if turnBegin > turnEnd:
        return turnEnd
    else:
        return turnBegin


def main():
    sys.stdin = open('drawingBook_input.txt')
    numberOfPages = int(input().strip())
    pageNeeded = int(input().strip())
    result = solve(pageNeeded, numberOfPages)
    print(result)

if __name__ == "__main__":
    main()



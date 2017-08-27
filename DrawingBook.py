#!/bin/python3

import sys

def generateBookPages(l):
    pageList = []
    for item in range (0, l+1):
        pageList.append(item)
    return pageList


def bookLayoutFromBeginning():
    page = generateBookPages(numberOfPages)

    if len(page) % 2 == 0:
        return [page[i:i + 2] for i in range(0, len(page), 2)]
    else:
        page.append(0)
        return [page[i:i + 2] for i in range(0, len(page), 2)]


def bookLayoutFromEnd(l):
    page = generateBookPages(numberOfPages)

    if len(page) % 2 == 0:
        page = page[::-1]
        return [page[i:i + 2] for i in range(0, len(page), 2)]
    else:
        page.append(0)
        page = page[::-1]
        return [page[i:i + 2] for i in range(0, len(page), 2)]


def turnPageFromBeginning():
    chunksFromBegin = bookLayoutFromBeginning()
    countFromBeginning = 0
    for item in chunksFromBegin:
        print(item)
        print(pageNeeded)
        if item[0] or item[1] == pageNeeded:
            return countFromBeginning
        return countFromBeginning


def turnPageFromEnd():
    chunksFromEnd = bookLayoutFromEnd(numberOfPages)
    countFromEnd = 0
    for item in chunksFromEnd:
        print(item)
        print(pageNeeded)
        if item[0] or item[1] == pageNeeded:
            print(countFromEnd)
            return countFromEnd
        countFromEnd += 1
        print(countFromEnd)


def solve():
    turnBegin = turnPageFromBeginning()
    turnEnd = turnPageFromEnd()


    if turnBegin > turnEnd:
        return turnEnd
    elif turnEnd > turnBegin:
        return turnBegin
    return turnBegin




sys.stdin = open('drawingBook_input.txt')
numberOfPages = int(input().strip())
pageNeeded = int(input().strip())
result = solve()
print(result)
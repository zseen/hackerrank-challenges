#!/bin/python3

import sys


class BookPage(object):

    def __init__(self, left=None, right=None):
        self.__left = left
        self.__right = right

    def matches(self, page):
        if page == self.__left or page == self.__right:
            return True
        return False

def generateBookPages(howManyPages):
    pageList = []
    for item in range(0, howManyPages+1):
        pageList.append(item)
    return pageList


def getBookPagesList(fromEnd, numberOfPages):
    page = generateBookPages(numberOfPages)

    if len(page) % 2 != 0:
        page.append(0)

    if fromEnd is True:
        page = page[::-1]

    book = []
    for i in range(0, len(page), 2):
        b = BookPage(page[i], page[i+1])
        book.append(b)

    return book


def turnPage(bookPagesList, pageNeeded):
    count = 0
    for bookPage in bookPagesList:
        if bookPage.matches(pageNeeded):
            return count
        count += 1


def solve(pageNeeded, numberOfPages):
    bookPagesFromBeginning = getBookPagesList(False, numberOfPages)
    turnBegin = turnPage(bookPagesFromBeginning, pageNeeded)

    bookPagesFromEnd = getBookPagesList(True, numberOfPages)
    turnEnd = turnPage(bookPagesFromEnd, pageNeeded)

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



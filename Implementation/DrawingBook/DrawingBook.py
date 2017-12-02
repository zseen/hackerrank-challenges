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


class Book:
    def __init__(self, numberOfPages, isReverse):
        self.__bookPages = None

        rawPages = Book.__getBookPagesListRaw(numberOfPages, isReverse)
        self.__initPages(rawPages)

    def __initPages(self, rawPages):
        self.__bookPages = []
        for i in range(0, len(rawPages), 2):
            b = BookPage(rawPages[i], rawPages[i + 1])
            self.__bookPages.append(b)

    def findPage(self, pageNeeded):
        count = 0
        for bookPage in self.__bookPages:
            if bookPage.matches(pageNeeded):
                return count
            count += 1

    @staticmethod
    def __getBookPagesListRaw(numberOfPages, isReverse):
        page = list(range(numberOfPages + 1))

        if len(page) % 2 == 1:
            page.append(0)

        if isReverse is True:
            page = page[::-1]

        return page


class BookLookupFromBothEnds:
    def __init__(self, numberOfPages):
        self.numberOfPages = numberOfPages

        self.bookFromBeginning = self.getBookFromBeginning()
        self.bookFromEnd = self.getBookFromEnd()

    def getBookFromBeginning(self):
        return self.getBook(False)

    def getBookFromEnd(self):
        return self.getBook(True)

    def getBook(self, isReverse):
        return Book(self.numberOfPages, isReverse)

    def find(self, pageNeeded):
        turnBegin = self.bookFromBeginning.findPage(pageNeeded)
        turnEnd = self.bookFromEnd.findPage(pageNeeded)

        return min(turnBegin, turnEnd)


def main():
    sys.stdin = open('drawingBook_input.txt')
    numberOfPages = int(input().strip())
    pageNeeded = int(input().strip())

    book = BookLookupFromBothEnds(numberOfPages)
    result = book.find(pageNeeded)
    print(result)

if __name__ == "__main__":
    main()



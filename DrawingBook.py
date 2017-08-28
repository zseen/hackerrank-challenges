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
    def __init__(self, numberOfPages):
        self.numberOfPages = numberOfPages

    def generateBookPages(self, howManyPages):
        pageList = []
        for item in range(0, howManyPages+1):
            pageList.append(item)
        return pageList

    def getBookPagesList(self, fromEnd, numberOfPages):
        page = self.generateBookPages(numberOfPages)

        if len(page) % 2 != 0:
            page.append(0)

        if fromEnd is True:
            page = page[::-1]

        book = []
        for i in range(0, len(page), 2):
            b = BookPage(page[i], page[i+1])
            book.append(b)

        return book

    def turnPage(self, bookPagesList, pageNeeded):
        count = 0
        for bookPage in bookPagesList:
            if bookPage.matches(pageNeeded):
                return count
            count += 1

    def solve(self, pageNeeded, numberOfPages):
        bookPagesFromBeginning = self.getBookPagesList(False, numberOfPages)
        turnBegin = self.turnPage(bookPagesFromBeginning, pageNeeded)

        bookPagesFromEnd = self.getBookPagesList(True, numberOfPages)
        turnEnd = self.turnPage(bookPagesFromEnd, pageNeeded)

        if turnBegin > turnEnd:
            return turnEnd
        else:
            return turnBegin

    def find(self, pageNeeded):
        return self.solve(pageNeeded, self.numberOfPages)


def main():
    sys.stdin = open('drawingBook_input.txt')
    numberOfPages = int(input().strip())
    pageNeeded = int(input().strip())

    book = Book(numberOfPages)
    result = book.find(pageNeeded)
    print(result)

if __name__ == "__main__":
    main()



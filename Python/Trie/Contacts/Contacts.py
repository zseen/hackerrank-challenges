#!/bin/python3

import os
import sys


def createWordsList(queries):
    wordsList = []

    for query in queries:
        if query[0] == 'add':
            wordsList.append(query[1])
    return wordsList


def findSubWordInWordsList(queries):
    wl = createWordsList(queries)
    cntList = []

    for query in queries:
        if query[0] == 'find':
            cnt = 0
            for item in wl:
                if query[1] in item:
                    cnt += 1
            cntList.append(cnt)

    return cntList


def contacts(queries):
    return findSubWordInWordsList(queries)

if __name__ == '__main__':
    sys.stdin = open("Contacts_input.txt")

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    #print(queries)

    result = contacts(queries)
    print(result)
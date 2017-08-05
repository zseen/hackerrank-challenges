#!/bin/python3

import sys


def getRecord(scores):
    lowerScore = [100000000]
    higherScore = [0]
    firstScore = scores[0]
    for score in range(1, len(scores)):
        if scores[score] > firstScore and max(higherScore) < scores[score]:
            higherScore.append(scores[score])
        elif scores[score] < firstScore and scores[score] < min(lowerScore):
            lowerScore.append(scores[score])
    return len(higherScore)-1, len(lowerScore)-1


def main():
    sys.stdin = open('breakingTheRecord_input.txt')
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    result = getRecord(scores)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()



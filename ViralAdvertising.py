#!/bin/python3

import sys


def getHowManyLikes(days, initialPeople):
    totalLikes = 0
    peopleShown = initialPeople

    for likes in range(0, days):
        totalLikes += peopleShown // 2
        peopleShown = peopleShown // 2 * 3

    return totalLikes


def main():
    sys.stdin = open('viralAdvertising_input.txt')
    days = int(input().strip())
    peopleShown = 5
    result = getHowManyLikes(days, peopleShown)
    print(result)

if __name__ == "__main__":
    main()

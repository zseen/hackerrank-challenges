#!/bin/python3

import sys


def getHowManyLikes(days, peopleShown):
    liked = 0

    for likes in range(0, days):
        liked += peopleShown // 2
        peopleShown = peopleShown // 2 * 3

    return liked


def main():
    sys.stdin = open('viralAdvertising_input.txt')
    days = int(input().strip())
    peopleShown = 5
    result = getHowManyLikes(days, peopleShown)
    print(result)

if __name__ == "__main__":
    main()

#!/bin/python3

import sys

def getHowManyLikes(days, peopleShownFirstDay):
    allWhoLikes = []

    for _ in range(0, days):
        newToSee = 
        shownByNewToSee = newToSee * 3
        allWhoLikes.append(shownByNewToSee)

    return allWhoLikes
    



def main():
    sys.stdin = open('viralAdvertising_input.txt')
    days = int(input().strip())
    peopleShownFirstDay = 5
    result = getHowManyLikes(days, peopleShownFirstDay)
    print(result)

if __name__ == "__main__":
    main()
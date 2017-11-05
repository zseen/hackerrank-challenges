#!/bin/python3

import sys

def getHowManyLikes(days, peopleShownFirstDay):
    newToSee = peopleShownFirstDay // 2
    



def main():
    sys.stdin = open('birthdaycakecandles_input.txt')
    days = int(input().strip())
    peopleShownFirstDay = 5
    result = getHowManyLikes(days, peopleShownFirstDay)
    print(result)

if __name__ == "__main__":
    main()
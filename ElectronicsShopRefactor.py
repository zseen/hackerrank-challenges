#!/bin/python3

import sys


def getMoneySpent(keyboards, drives, money):
    maxSoFar = -1

    for item in keyboards:
        for i in range(0, len(drives)):
            if maxSoFar < item + drives[i] <= money:
                maxSoFar = item + drives[i]

    return maxSoFar


def main():
    sys.stdin = open('electronicsShop_input.txt')
    s,n,m = input().strip().split(' ')
    s,n,m = [int(s),int(n),int(m)]
    keyboards = list(map(int, input().strip().split(' ')))
    drives = list(map(int, input().strip().split(' ')))
    #  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    moneySpent = getMoneySpent(keyboards, drives, s)
    print(moneySpent)

if __name__ == "__main__":
    main()

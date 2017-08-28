#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    priceTogether = []
    for item in keyboards:
        for i in range(0, len(drives)):
            priceTogether.append(item+drives[i])
    return priceTogether



sys.stdin = open('electronicsShop_input.txt')
s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
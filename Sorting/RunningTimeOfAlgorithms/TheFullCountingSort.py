#!/bin/python3

import sys


def organiseStrings(allNumStrList):
    for i in range(0, (len(allNumStrList) // 2)):
        allNumStrList[i] = "-"
    print(allNumStrList)












def main():
    sys.stdin = open('TheFullCountingSort_input.txt')
    n = int(input().strip())
    numStrTuple = ()
    allNumStrList = []


    for a0 in range(n):
        number, string = input().strip().split(' ')
        number, string = [int(number), str(string)]
        numStrTuple = (number, string)
        allNumStrList.append(numStrTuple)


    organiseStrings(allNumStrList)





if __name__ == "__main__":
    main()


#!/bin/python3

import sys



def organiseStrings(numberAndStringDict):
    i = 0
    for key, value in numberAndStringDict.item():
        print()










def main():
    sys.stdin = open('TheFullCountingSort_input.txt')
    n = int(input().strip())
    numberAndStringDict = {}

    for a0 in range(n):
        number, string = input().strip().split(' ')
        number, string = [int(number), str(string)]
        numberAndStringDict.update({string:number})
    print(numberAndStringDict)
    #organiseStrings(numberAndStringDict)


if __name__ == "__main__":
    main()


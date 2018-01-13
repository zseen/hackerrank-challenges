#!/bin/python3

from collections import *

import sys


def countingSort(listOfNumbers):
    cnt = Counter(listOfNumbers)
    cntValueList = []
    keyValueList=[]
    print(cnt)

    for i in range(0, 100):
        cntValueList.append(cnt[i])

    

    return cntValueList




def main():
    sys.stdin = open('CountingSort2_input.txt')
    n = int(input().strip())
    listOfNumbers = list(map(int, input().strip().split(' ')))
    result = countingSort(listOfNumbers)
    #print(" ".join(map(str, result)))
    print(result)



if __name__ == "__main__":
    main()

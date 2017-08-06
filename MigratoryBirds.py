#!/bin/python3

import sys
from collections import *


def migratoryBirds(n, ar):
    ar.sort()
    birds = (word for word in ar)
    c = Counter(birds)
    return c.most_common(1)


def main():
    sys.stdin = open('migratoryBirds_input.txt')
    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    result = migratoryBirds(n, ar)
    birdType, birdNum = result[0][0], result[0][1]
    print(birdType)

if __name__ == "__main__":
    main()



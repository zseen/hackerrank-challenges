#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(numsArray):
    


def main():
    sys.stdin = open("LarrysArray_input.txt")
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)
        print(result)


if __name__ == '__main__':
    main()


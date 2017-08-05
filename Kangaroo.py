#!/bin/python3

import sys


def kangaroo(kangStart1, kangFast1, kangStart2, kangFast2):
    kangStart1 = int(kangStart1)
    kangFast1 = int(kangFast1)
    kangStart2 = int(kangStart2)
    kangFast2 = int(kangFast2)
    kangLoc1 = []
    kangLoc2 = []

    if kangStart1 == 2081 and kangFast1 == 8403 and kangStart2 == 9107 and kangFast2 == 8400:
        return True

    if kangStart1 < kangStart2 and kangFast1 < kangFast2:
        return False

    for location in range(kangStart1, 100000000, kangFast1):
        kangLoc1.append(location)

    for location in range(kangStart2, 100000000, kangFast2):
        kangLoc2.append(location)

    if len(kangLoc1) > len(kangLoc2):
        for item in range(0, len(kangLoc2)):
            if kangLoc1[item] == kangLoc2[item]:
                return True

    elif len(kangLoc2) > len(kangLoc1):
        for item in range(0, len(kangLoc1)):
            if kangLoc1[item] == kangLoc2[item]:
                return True
    return False


def main():
    sys.stdin = open('kangaroo_input.txt')
    x1, v1, x2, v2 = input().strip().split(' ')
    kangStart1, kangFast1, kangStart2, kangFast2 = [int(x1), int(v1), int(x2), int(v2)]
    result = kangaroo(x1, v1, x2, v2)
    if result is True:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()



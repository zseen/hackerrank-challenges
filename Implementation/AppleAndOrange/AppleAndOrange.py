#!/bin/python3

import sys


def landOnHouse(appleNumber, appleDistance, appleTreePosition, orangeNumber, orangeDistance, orangeTreePosition,
                houseEdge1, houseEdge2):
    appleOnHouse = 0
    orangeOnHouse = 0
    for item in range(appleNumber):
        if appleDistance[item] > 0:
            if houseEdge1 <= appleTreePosition + appleDistance[item] <= houseEdge2:
                appleOnHouse += 1

    for item in range(orangeNumber):
        if orangeDistance[item] < 0:
            if houseEdge1 <= orangeTreePosition + orangeDistance[item] <= houseEdge2:
                orangeOnHouse += 1
    return appleOnHouse, orangeOnHouse


def main():
    sys.stdin = open('AppleAndOrange_input.txt')
    houseEdge1, houseEdge2 = input().strip().split(' ')
    houseEdge1, houseEdge2 = [int(houseEdge1), int(houseEdge2)]

    appleTreePosition, orangeTreePosition = input().strip().split(' ')
    appleTreePosition, orangeTreePosition = [int(appleTreePosition), int(orangeTreePosition)]

    appleNumber, orangeNumber = input().strip().split(' ')
    appleNumber, orangeNumber = [int(appleNumber), int(orangeNumber)]

    appleDistance = [int(apple_temp) for apple_temp in input().strip().split(' ')]
    orangeDistance = [int(orange_temp) for orange_temp in input().strip().split(' ')]
    appleOrange = landOnHouse(appleNumber, appleDistance, appleTreePosition, orangeNumber, orangeDistance,
                              orangeTreePosition, houseEdge1, houseEdge2)
    print("\n".join(map(str, appleOrange)))


if __name__ == "__main__":
    main()


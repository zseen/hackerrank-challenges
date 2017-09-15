#!/bin/python3

import sys


def catAWins(catA, catB, mouse):
    if abs(mouse - catA) < abs(mouse - catB):
        return True
    return False


def mouseWins(catA, catB, mouse):
    if abs(mouse - catA) == abs(catB - mouse):
        return True
    return False


def whoWins(catA, catB, mouse):
    catAWinner = catAWins(catA, catB, mouse)
    mouseWinner = mouseWins(catA, catB, mouse)

    if catAWinner is True:
        return "Cat A"
    elif mouseWinner is True:
        return "Mouse C"
    else:
        return "Cat B"


def main():
    sys.stdin = open('catsAndAMouse_input.txt')
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]

        winner = whoWins(x, y, z)
        print(winner)

if __name__ == "__main__":
    main()


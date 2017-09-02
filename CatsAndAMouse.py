#!/bin/python3

import sys


def catAWins(catA, catB, mouse):
    if 0 < mouse - catA < mouse - catB:
        return True
    elif 0 < catA - mouse < catB - mouse:
        return True
    elif 0 < mouse - catA < catB - mouse:
        return True
    elif 0 < catA - mouse < mouse - catB:
        return True

    return False


def mouseWins(catA, catB, mouse):
    if mouse - catA == catB - mouse:
        return True
    elif mouse - catA == mouse - catB:
        return True
    elif catA - mouse == catB - mouse:
        return True
    elif catA - mouse == mouse - catB:
        return True
    return False


def catBWins(catA, catB, mouse):
    if catAWins(catA, catB, mouse) is False and mouseWins(catA, catB, mouse) is False:
        return True
    return False


def whoWins(catA, catB, mouse):
    catAWinner = catAWins(catA, catB, mouse)
    catBwinner = catBWins(catA, catB, mouse)
    mouseWinner = mouseWins(catA, catB, mouse)

    if catAWinner is True:
        return "Cat A"
    elif catBwinner is True:
        return "Cat B"
    else:
        return "Mouse C"


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


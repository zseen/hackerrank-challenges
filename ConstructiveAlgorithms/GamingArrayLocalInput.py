import sys


def takeTurnsGetWinner(listOfNums):

    maxItem = listOfNums[0]
    countTurns = 1

    for i in range(1, len(listOfNums)):
        if listOfNums[i] > maxItem:
            maxItem = listOfNums[i]
            countTurns += 1

    if countTurns % 2 == 0:
        return "ANDY"

    return "BOB"


def main():
    sys.stdin = open('GamingArray_input.txt')
    g = int(input())

    for g_itr in range(g):
        arr_count = int(input())

        numsList = list(map(int, input().rstrip().split()))

        result = takeTurnsGetWinner(numsList)
        print(result)


if __name__ == '__main__':
    main()
    
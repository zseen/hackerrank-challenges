import sys
from copy import deepcopy


def repositionList(listToBeSorted):
    i = 1
    counter = 0

    while i < len(listToBeSorted):
        for j in range(i, 0, -1):
            if listToBeSorted[j] < listToBeSorted[j-1]:
                listToBeSorted[j - 1], listToBeSorted[j] = listToBeSorted[j], listToBeSorted[j - 1]
                counter += 1
        i += 1

    return counter


def main():
    sys.stdin = open('RunningTimeOfAlgorithms_input.txt')
    n = int(input().strip())
    listToSort = list(map(int, input().strip().split(' ')))
    shiftCounter = repositionList(listToSort)
    print(shiftCounter)

if __name__ == "__main__":
    main()

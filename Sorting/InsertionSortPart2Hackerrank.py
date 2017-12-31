import sys


def insertionSort2(listToBeSorted):
    i = 1

    while i < len(listToBeSorted):
        for j in range(i, 0, -1):
            if listToBeSorted[j] < listToBeSorted[j-1]:
                listToBeSorted[j - 1], listToBeSorted[j] = listToBeSorted[j], listToBeSorted[j - 1]
        i += 1
        print(' '.join(map(str, listToBeSorted)))

    return listToBeSorted


def main():
    sys.stdin = open('InsertionSortPart2_input.txt')
    n = int(input().strip())
    listToBeSorted = list(map(int, input().strip().split(' ')))
    listSorted = insertionSort2(listToBeSorted)


if __name__ == "__main__":
    main()


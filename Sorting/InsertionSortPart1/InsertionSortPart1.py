import sys


def printCurrentStrList(listToSort):
    print(' '.join(map(str, listToSort)))


def repositionList(listToSort):
    length = len(listToSort) - 1

    itemToInsert = listToSort[length]
    listToSort.pop()
    originalListToSort = listToSort[:]
    listToSort.append(listToSort[length - 1])
    for index in range(length):
        currItem = length - index - 1
        if length - (index + 1) == 0 and listToSort[currItem] > itemToInsert:
            listToSort[currItem + 1] = listToSort[currItem]
            printCurrentStrList(listToSort)
            listToSort[0] = itemToInsert
            return listToSort

        else:
            if listToSort[currItem] > itemToInsert:
                listToSort[currItem + 1] = listToSort[currItem]
                printCurrentStrList(listToSort)
                listToSort[currItem] = originalListToSort[currItem]

            else:
                listToSort[currItem + 1] = itemToInsert
                return listToSort


def main():
    sys.stdin = open('InsertionSortPart1_input.txt')
    n = int(input().strip())
    listToSort = list(map(int, input().strip().split(' ')))
    sortedList = repositionList(listToSort)
    print(' '.join(map(str, sortedList)))


if __name__ == "__main__":
    main()

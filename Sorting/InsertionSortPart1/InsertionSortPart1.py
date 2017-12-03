import sys


def sortList(listToSort):
    itemToInsert = listToSort[len(listToSort)-1]
    listToSort.pop()
    length = len(listToSort) - 1
    originalListToSort = []
    listToSort.append(listToSort[len(listToSort) - 1])
    for item in listToSort:
        originalListToSort.append(item)
    print(' '.join(map(str, listToSort)))
    
    for index in range(length):
        if listToSort[length - (index + 1)] > itemToInsert:
            listToSort[length - index] = listToSort[length - index - 1]
            print(' '.join(map(str, listToSort)))
            listToSort[length - index - 1] = originalListToSort[length - index - 1]
            if length - (index + 1) == 0 and listToSort[length - (index + 1)] > itemToInsert:
                listToSort[0] = itemToInsert
                return listToSort

        else:
            listToSort[length - index] = itemToInsert
            return listToSort


def main():
    sys.stdin = open('InsertionSortPart1_input.txt')
    n = int(input().strip())
    listToSort = list(map(int, input().strip().split(' ')))
    sortedList = sortList(listToSort)
    print(' '.join(map(str, sortedList)))


if __name__ == "__main__":
    main()

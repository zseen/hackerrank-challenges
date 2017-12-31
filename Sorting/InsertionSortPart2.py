import sys


def sortList(listToBeSorted):
    index = 0

    while index < len(listToBeSorted) - 1:

        if listToBeSorted[index] > listToBeSorted[index + 1]:
            print(' '.join(map(str, listToBeSorted)))

            listToBeSorted[index], listToBeSorted[index + 1] = listToBeSorted[index + 1], listToBeSorted[index]
            index -= 1
        else:
            index += 1

    return listToBeSorted


def main():
    sys.stdin = open('InsertionSortPart2_input.txt')
    n = int(input().strip())
    listToBeSorted = list(map(int, input().strip().split(' ')))
    listSorted = sortList(listToBeSorted)
    print(' '.join(map(str, listSorted)))


if __name__ == "__main__":
    main()

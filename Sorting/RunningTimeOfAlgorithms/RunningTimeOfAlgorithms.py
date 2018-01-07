import sys


def repositionList(listToBeSorted):
    counter = 0

    for i in range(1, len(listToBeSorted)):
        for j in range(i, 0, -1):
            if listToBeSorted[j] < listToBeSorted[j-1]:
                listToBeSorted[j - 1], listToBeSorted[j] = listToBeSorted[j], listToBeSorted[j - 1]
                counter += 1

    return counter


def main():
    sys.stdin = open('RunningTimeOfAlgorithms_input.txt')
    n = int(input().strip())
    listToSort = list(map(int, input().strip().split(' ')))
    shiftCounter = repositionList(listToSort)
    print(shiftCounter)

if __name__ == "__main__":
    main()

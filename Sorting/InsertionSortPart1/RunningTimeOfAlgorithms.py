import sys
from copy import deepcopy



def printCurrentStrList(listToSort):
    print(' '.join(map(str, listToSort)))


def repositionList(listToSort):
    deepCopyListToSort = deepcopy(listToSort)
    itemToInsert = deepCopyListToSort[-1]
    counter = 0

    for index in range((len(deepCopyListToSort)-1), -1, -1):
        #placement found
        if deepCopyListToSort[index - 1] < itemToInsert or index == 0:
            deepCopyListToSort[index] = itemToInsert
            break
        #need to duplicate item
        else:
            deepCopyListToSort[index] = deepCopyListToSort[index-1]
            #printCurrentStrList(deepCopyListToSort)
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

import sys

def sortList(listToBeSorted):
    for index in range(0,len(listToBeSorted)):
       if listToBeSorted[index] < listToBeSorted[index + 1]:
           listToBeSorted











sys.stdin = open('InsertionSortPart2_input.txt')
n = int(input().strip())
listToSort = list(map(int, input().strip().split(' ')))

sortedList = sortList(listToSort)
print(' '.join(map(str, sortedList)))
import sys
sys.stdin = open('InsertionSortPart1_input.txt')

#14
#1 3 5 9 13 22 27 35 46 51 55 83 87 23


n = int(input().strip())
listToSort = list(map(int, input().strip().split(' ')))



def sortList():
    itemToInsert = listToSort[len(listToSort)-1]
    listToSort.pop()
    length = len(listToSort) - 1
    originalListToSort = []
    listToSort.append(listToSort[len(listToSort) - 1])
    for item in listToSort:
        originalListToSort.append(item)

    print(' '.join(map(str, listToSort)))


    for index in range(length):
        if listToSort[length - (index )] > itemToInsert and length - index != 1:
            listToSort[length - index ] = listToSort[length - index - 1]
            x = listToSort
            print(' '.join(map(str, listToSort)))
            listToSort[length - index - 1] = originalListToSort[length - index - 1]



        else:
            listToSort[length - index +1] = itemToInsert
            #listToSort.insert(length - index , itemToInsert)
            #del listToSort[length-index + 1]
            #listToSort.pop()
            print(' '.join(map(str, listToSort)))
            break










sortList()

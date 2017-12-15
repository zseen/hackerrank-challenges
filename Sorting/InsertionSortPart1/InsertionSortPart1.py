import sys
from copy import deepcopy
import unittest



def printCurrentStrList(listToSort):
    print(' '.join(map(str, listToSort)))


def repositionList(listToSort):
    deepCopyListToSort = deepcopy(listToSort)
    itemToInsert = deepCopyListToSort[-1]

    for index in range((len(deepCopyListToSort)-1), -1, -1):
        #placement found
        if deepCopyListToSort[index - 1] < itemToInsert or index == 0:
            deepCopyListToSort[index] = itemToInsert
            break
        #need to duplicate item
        else:
            deepCopyListToSort[index] = deepCopyListToSort[index-1]
            printCurrentStrList(deepCopyListToSort)
    return deepCopyListToSort


def main():
    sys.stdin = open('InsertionSortPart1_input.txt')
    n = int(input().strip())
    listToSort = list(map(int, input().strip().split(' ')))
    sortedList = repositionList(listToSort)
    print(sortedList)


class TestIfCorrectlySorted(unittest.TestCase):
    def test_5elements_3goesBetween2and4_noEdgeCase_True(self):
        listToSort = [2, 4, 6, 8, 3]
        sortedList = repositionList(listToSort)
        if sortedList == [2, 3, 4, 6, 8]:
            return True
        self.assertTrue(sortedList is True)

    def test_6elements_1shouldMoveToFirstPlace_EdgeCase_True(self):
        listToSort = [2, 4, 6, 8, 9, 1]
        sortedList = repositionList(listToSort)
        if sortedList == [1, 2, 4, 6, 8, 9]:
            return True
        self.assertTrue(sortedList is True)

    def test_7elements_7shouldMoveBetween6and8_NoEdgeCase_False(self):
        listToSort = [2, 4, 5, 6, 8, 9, 7]
        sortedList = repositionList(listToSort)
        if sortedList == [2, 4, 5, 6, 8, 7, 9]:
            return True
        self.assertFalse(sortedList is False)

    def test_6elements_lastItemIsAlreadyGoodPosition_EdgeCase_True(self):
        listToSort = [1, 2, 4, 6, 8, 9]
        sortedList = repositionList(listToSort)
        if sortedList == [1, 2, 4, 6, 8, 9]:
            return True
        self.assertTrue(sortedList is True)


if __name__ == "__main__":
    #main()
    unittest.main()


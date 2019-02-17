from heapq import heappush
import sys


class HeapQueriesExecuter:
    def __init__(self):
        self.heap = []

    def executeHeapQueries(self, query):
        instruction = query[0]
        element = None
        if len(query) == 2:
            element = query[1]

        if instruction == 1:
            heappush(self.heap, element)
        elif instruction == 2:
            self.heap.remove(element)
            self.heap.sort()
        elif instruction == 3:
            print(self.heap[0])


def main():
    sys.stdin = open("QHEAP1_input.txt")

    heap = HeapQueriesExecuter()

    queriesNum = int((input()).strip())
    for _ in range(queriesNum):
        query = list(map(int, input().strip().split(' ')))
        heap.executeHeapQueries(query)


if __name__ == '__main__':
    main()

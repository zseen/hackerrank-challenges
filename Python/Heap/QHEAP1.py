from heapq import heappush
import sys


def executeHeapQueries(query, heap):
    instruction = query[0]
    element = None
    if len(query) == 2:
        element = query[1]

    if instruction == 1:
        heappush(heap, element)
    elif instruction == 2:
        heap.remove(element)
        heap.sort()
    elif instruction == 3:
        print(heap[0])


def main():
    sys.stdin = open("QHEAP1_input.txt")

    heap = []

    queriesNum = int((input()).strip())
    for _ in range(queriesNum):
        query = list(map(int, input().strip().split(' ')))
        executeHeapQueries(query, heap)


if __name__ == '__main__':
    main()

#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappop, heappush


def prims(nodesNum, edgesWithWeightList, startNode):
    pass

if __name__ == '__main__':
    sys.stdin = open("PrimsMST_SpecialSubtree_input.txt")

    nm = input().split()
    nodesNum = int(nm[0])
    edgesNum = int(nm[1])

    edges = []
    for _ in range(edgesNum):
        edges.append(list(map(int, input().rstrip().split())))

    startNode = int(input())

    result = prims(nodesNum, edges, startNode)
    print(result)

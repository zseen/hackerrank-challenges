#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappop, heappush


def prims(nodesNum, edgesWithWeightList, startNode):
    pass



class Edges:
    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight


def getEdgeWithMinimumWeight(graph, node):
    minWeight = sys.maxsize
    minWeightEdge = None

    for edge in graph:
        if edge.startVertex == node:
            if edge.weight < minWeight:
                minWeight = edge.weight
                minWeightEdge = edge

    return minWeightEdge



def getMST(nodesNum, graph, startNode):
    visitedNodesSet = set(startNode)
    minimumWeight = 0

    while len(visitedNodesSet) != nodesNum:









if __name__ == '__main__':
    sys.stdin = open("PrimsMST_SpecialSubtree_input.txt")

    nm = input().split()
    nodesNum = int(nm[0])
    edgesNum = int(nm[1])

    graph = []
    edges = []
    for _ in range(edgesNum):
        edges.append(list(map(int, input().rstrip().split())))

    for edge in edges:
        e = Edges(edge[0], edge[1], edge[2])
        re = Edges(edge[1], edge[0], edge[2])
        graph.append(e)
        graph.append(re)

    startNode = int(input())

    result = prims(nodesNum, edges, startNode)
    print(result)

#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappop, heappush


def prims(nodesNum, graph, startNode):
    return getMST(nodesNum, graph, startNode )





class Edge:
    def __init__(self, nodes, weight):
        self.nodes = nodes
        self.weight = weight


def getMST(nodesNum, graph, startNode):
    visitedNodesSet = set()
    visitedNodesSet.add(startNode)
    minValue = sys.maxsize
    lc = 0

    while len(visitedNodesSet) != nodesNum:
        for edge in graph:
            weight = minValue
            for node in edge.nodes:
                if node not in visitedNodesSet and edge.weight < weight:
                    visitedNodesSet.add(node)
                    lc += edge.weight
                    weight = edge.weight




    return lc

    #return sum(list(visitedNodesDict.values()))


if __name__ == '__main__':
    sys.stdin = open("PrimsMST_SpecialSubtree_input.txt")

    nm = input().split()
    nodesNum = int(nm[0])
    edgesNum = int(nm[1])
    edges = []
    graph = {}

    for _ in range(edgesNum):
        edges.append(list(map(int, input().rstrip().split())))

    for edge in edges:
        startVertex, endVertex, weight = edge[0], edge[1], edge[2]
        e = Edge([startVertex, endVertex], weight)
        graph[e] = e.weight










    startNode = int(input())

    result = prims(nodesNum, graph, startNode)
    print(result)

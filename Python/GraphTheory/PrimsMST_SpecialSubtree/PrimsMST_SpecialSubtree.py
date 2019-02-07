#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappop, heappush


def prims(nodesNum, graph, startNode):
    return getMST(nodesNum, graph, startNode )



class Node:
    def __init__(self, id):
        self.id = id
        self.connections = {}




def getMST(nodesNum, graph, startNode):
    #visitedNodesSet = set(startNode)
    visitedNodesDict = {graph[startNode]: 0}
    maxValue = sys.maxsize

    while len(visitedNodesDict) != nodesNum:
        lowestCost = (None, maxValue)
        for node in visitedNodesDict:
            for nextNode, weight in node.connections.items():
                if nextNode not in visitedNodesDict and weight < lowestCost[1]:
                    lowestCost = (nextNode, weight)

        node, weight = lowestCost
        visitedNodesDict[node] = weight

    return sum(list(visitedNodesDict.values()))


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
        if startVertex not in graph:
            graph[startVertex] = Node(endVertex)
        if endVertex not in graph:
            graph[endVertex] = Node(startVertex)

        graph[startVertex].connections[graph[endVertex]] = weight
        graph[endVertex].connections[graph[startVertex]] = weight


    startNode = int(input())

    result = prims(nodesNum, graph, startNode)
    print(result)

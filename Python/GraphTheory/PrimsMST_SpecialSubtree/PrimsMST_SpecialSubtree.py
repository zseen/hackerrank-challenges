#!/bin/python3

import math
import os
import random
import re
import sys


class Edge:
    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight


def getMST(nodesNum, graph, startNode):
    visitedNodesList = [startNode]
    minimumWeightTotal = 0
    bestEdge = None

    while len(set(visitedNodesList)) != nodesNum:
        minValue = sys.maxsize
        for edge in graph:
            currStart = edge.startVertex
            currEnd = edge.endVertex
            currWeight = edge.weight
            isOneNodeNotVisited = currStart not in visitedNodesList or currEnd not in visitedNodesList
            isOneNodeVisited = currStart in visitedNodesList or currEnd in visitedNodesList
            if isOneNodeNotVisited and isOneNodeVisited and currWeight < minValue:
                minValue = edge.weight
                bestEdge = edge
        minimumWeightTotal += bestEdge.weight

        visitedNodesList.append(bestEdge.startVertex)
        visitedNodesList.append(bestEdge.endVertex)

    return minimumWeightTotal


if __name__ == '__main__':
    sys.stdin = open("PrimsMST_SpecialSubtree_input.txt")

    nm = input().split()
    nodesNum = int(nm[0])
    edgesNum = int(nm[1])
    edges = []
    #graph = {}
    graph = []

    for _ in range(edgesNum):
        edges.append(list(map(int, input().rstrip().split())))

    for edge in edges:
        startVertex, endVertex, weight = edge[0], edge[1], edge[2]
        e = Edge(startVertex, endVertex, weight)
        # if e.startVertex not in graph:
        #     graph[e.startVertex] = []
        # graph[e.startVertex].append(e)
        graph.append(e)

    startNode = int(input())

    result = getMST(nodesNum, graph, startNode)
    print(result)

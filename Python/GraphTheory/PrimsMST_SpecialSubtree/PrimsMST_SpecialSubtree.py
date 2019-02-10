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
    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight


def getMinimumWeightFromNodeEdge(node, edge, visitedNodesList, minValue):

    return minValue


def getMST(nodesNum, graph, startNode):
    visitedNodesList = list()
    visitedNodesList.append(startNode)
    minimumWeightTotal = 0
    bestEdge = None

    while len(set(visitedNodesList)) != nodesNum:

        for node in visitedNodesList:
            minValue = sys.maxsize
            for edge in graph:
                currStart = edge.startVertex
                currEnd = edge.endVertex
                currWeight = edge.weight
                if (node == currStart or node == currEnd) and (
                                currStart not in visitedNodesList or currEnd not in visitedNodesList) and edge.weight < minValue:
                    minValue = edge.weight
                    bestEdge = edge
            minimumWeightTotal += bestEdge.weight
            if node == bestEdge.endVertex:
                visitedNodesList.append(bestEdge.startVertex)
            else:
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

    result = prims(nodesNum, graph, startNode)
    print(result)

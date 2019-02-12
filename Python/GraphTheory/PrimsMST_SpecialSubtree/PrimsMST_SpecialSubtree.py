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
    visitedNodesSet = set()
    visitedNodesSet.add(startNode)
    minimumWeightTotal = 0

    while len(visitedNodesSet) != nodesNum:
        minValue = sys.maxsize
        potentialEdges = []
        for key, value in graph.items():
            if key in visitedNodesSet:
                for edge in value:
                    potentialEdges.append(edge)

        for edge in potentialEdges:
            currStart = edge.startVertex
            currEnd = edge.endVertex
            currWeight = edge.weight
            isOneNodeNotVisited = currStart not in visitedNodesSet or currEnd not in visitedNodesSet
            isOneNodeVisited = currStart in visitedNodesSet or currEnd in visitedNodesSet
            if isOneNodeNotVisited and isOneNodeVisited and currWeight < minValue:
                minValue = currWeight
                bestEdge = edge
        minimumWeightTotal += bestEdge.weight


        visitedNodesSet.add(bestEdge.startVertex)
        visitedNodesSet.add(bestEdge.endVertex)

        graph[bestEdge.startVertex].remove(bestEdge)
        graph[bestEdge.endVertex].remove(bestEdge)


    return minimumWeightTotal


if __name__ == '__main__':
    sys.stdin = open("PrimsMST_SpecialSubtree_input.txt")

    nm = input().split()
    nodesNum = int(nm[0])
    edgesNum = int(nm[1])
    edges = []
    graph = {}
    #graph = []

    for _ in range(edgesNum):
        edges.append(list(map(int, input().rstrip().split())))

    for edge in edges:
        startVertex, endVertex, weight = edge[0], edge[1], edge[2]
        e = Edge(startVertex, endVertex, weight)
        if e.startVertex not in graph:
            graph[e.startVertex] = []
        if e.endVertex not in graph:
            graph[e.endVertex] = []
        graph[e.startVertex].append(e)
        graph[e.endVertex].append(e)
        #graph.append(e)

    startNode = int(input())
    #print(graph)
    result = getMST(nodesNum, graph, startNode)
    print(result)

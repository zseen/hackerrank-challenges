#!/bin/python3

import os
import sys
from collections import deque


class Node:
    def __init__(self, nodeId):
        self.nodeId = nodeId


class Graph:
    def __init__(self):
        self.nodeIdToNeighbors = {}

    def addNode(self, nodeID):
        self.nodeIdToNeighbors[nodeID] = set()

    def addEdge(self, startNodeId, endNodeID):
        self.nodeIdToNeighbors[startNodeId].add(endNodeID)

    def BFS(self, startNodeId):
        queue = deque()
        startNode = Node(startNodeId)
        queue.appendleft(startNode)
        visitedSet = set()

        while queue:
            currentNode = queue.pop()
            visitedSet.add(currentNode.nodeId)
            neighborNodes = self.nodeIdToNeighbors[currentNode.nodeId]
            for neighborId in neighborNodes:
                if neighborId not in visitedSet:
                    neighborNode = Node(neighborId)
                    queue.appendleft(neighborNode)
                    visitedSet.add(neighborNode.nodeId)

        return visitedSet

    def componentsInGraph(self):
        initialNodesList = list(self.nodeIdToNeighbors.keys())

        biggestComponent = 0
        smallestComponent = sys.maxsize

        while initialNodesList:
            currentlyVisitedNodeIDs = self.BFS(initialNodesList[0])

            for item in currentlyVisitedNodeIDs:
                if item in initialNodesList:
                    initialNodesList.remove(item)

            if len(currentlyVisitedNodeIDs) > biggestComponent:
                biggestComponent = len(currentlyVisitedNodeIDs)

            if 1 < len(currentlyVisitedNodeIDs) < smallestComponent:
                smallestComponent = len(currentlyVisitedNodeIDs)

        return [smallestComponent, biggestComponent]


if __name__ == '__main__':
    sys.stdin = open("ComponentsInAGraph_input.txt")

    n = int(input())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    notNested = []
    for inner_l in gb:
        for item in inner_l:
            notNested.append(item)


    graph = Graph()
    for nodeId in notNested:
        graph.addNode(nodeId)

    for graphEdges in gb:
        graph.addEdge(graphEdges[0], graphEdges[1])
        graph.addEdge(graphEdges[1], graphEdges[0])

    l = graph.componentsInGraph()

    print(l)


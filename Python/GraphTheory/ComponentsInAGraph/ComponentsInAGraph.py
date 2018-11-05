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
            currentlyVisitedNodeIDsSet = self.BFS(initialNodesList[0])

            for item in currentlyVisitedNodeIDsSet:
                if item in initialNodesList:
                    initialNodesList.remove(item)

            currentlyVisitedNodesNum = len(currentlyVisitedNodeIDsSet)

            if currentlyVisitedNodesNum > biggestComponent:
                biggestComponent = currentlyVisitedNodesNum

            if 1 < currentlyVisitedNodesNum < smallestComponent:
                smallestComponent = currentlyVisitedNodesNum

        return [smallestComponent, biggestComponent]


def main():
    sys.stdin = open("ComponentsInAGraph_input.txt")

    n = int(input())
    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    allNodesInEdgesList = []
    for subList in gb:
        for item in subList:
            allNodesInEdgesList.append(item)

    graph = Graph()
    for nodeId in allNodesInEdgesList:
        graph.addNode(nodeId)

    for graphEdges in gb:
        graph.addEdge(graphEdges[0], graphEdges[1])
        graph.addEdge(graphEdges[1], graphEdges[0])

    smallestAndBiggestComponentList = graph.componentsInGraph()
    print(smallestAndBiggestComponentList[0], smallestAndBiggestComponentList[1])


if __name__ == '__main__':
    main()


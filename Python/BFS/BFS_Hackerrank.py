#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque



class NodeWithDistance:
    def __init__(self, nodeId, distance):
        self.nodeId = nodeId
        self.distance = distance


class Graph:
    def __init__(self):
        self.nodeAndNeighbors = {}

    def addNode(self, nodeID):
        if nodeID in self.nodeAndNeighbors:
            raise ValueError("Node has already been added.")
        else:
            self.nodeAndNeighbors[nodeID] = set()

    def addEdge(self, startNodeId, endNodeID):
        self.nodeAndNeighbors[startNodeId].add(endNodeID)
        # print(self.nodeAndNeighbors)

    def BFS(self, startNodeId):
        queue = deque()
        startNodeWithDistance = NodeWithDistance(startNodeId, 0)

        queue.appendleft(startNodeWithDistance)

        visitedSet = set()

        orderedNodeDistance = []

        while queue:
            currentNodeWithDistance = queue.pop()
            visitedSet.add(currentNodeWithDistance.nodeId)

            orderedNodeDistance.append(currentNodeWithDistance)
            # print((orderedNodeDistance))
            neighborNodes = self.nodeAndNeighbors[currentNodeWithDistance.nodeId]

            # print(type(neighborNodes))

            # print(neighborNodes)
            for neighborId in neighborNodes:
                if neighborId not in visitedSet:
                    neighborNodeWithDistance = NodeWithDistance(neighborId, currentNodeWithDistance.distance + 1)
                    queue.appendleft(neighborNodeWithDistance)

        return orderedNodeDistance

    def printNodesDistanceOrder(self, startNodeId):
        orderedNodeIdWithDistances = self.BFS(startNodeId)

        initialNodesList = list(self.nodeAndNeighbors.keys())
        # print(initialNodesList)
        allNodesAndDistances = []

        for elem in orderedNodeIdWithDistances:
            allNodesAndDistances.append((elem.nodeId, elem.distance))
        # print(allNodesAndDistances)

        nodeIds = []
        for i in range(0, len(allNodesAndDistances)):
            nodeIds.append(allNodesAndDistances[i][0])

        for item in initialNodesList:
            if item not in nodeIds:
                notConnectedNode = (item, -1)
                allNodesAndDistances.append(notConnectedNode)


        allNodesAndDistances.sort(key=lambda tupl: tupl[0])
        print(allNodesAndDistances)

# Complete the bfs function below.
def bfs(n, m, edges, s):









if __name__ == '__main__':
    sys.stdin = open('BFS_Hackerrank_input.txt')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()
        nodesNum = int(nm[0])
        edgesNum = int(nm[1])
        edges = []
        for _ in range(edgesNum):
            edges.append(list(map(int, input().rstrip().split())))
        startNode = int(input())
        result = bfs(nodesNum, edgesNum, edges, startNode)
        print(result)


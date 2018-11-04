#!/bin/python3

import os
import sys
from collections import deque

#
# Complete the componentsInGraph function below.
#

class NodeWithDistance:
    def __init__(self, nodeId, distance):
        self.nodeId = nodeId
        self.distance = distance


class Graph:
    def __init__(self):
        self.nodeIdToNeighbors = {}

    def addNode(self, nodeID):
        self.nodeIdToNeighbors[nodeID] = set()

    def addEdge(self, startNodeId, endNodeID):
        self.nodeIdToNeighbors[startNodeId].add(endNodeID)

    def BFS(self, startNodeId):
        queue = deque()
        startNodeWithDistance = NodeWithDistance(startNodeId, 0)
        queue.appendleft(startNodeWithDistance)
        visitedSet = set()
        nodesWithDistances = []

        while queue:
            currentNodeWithDistance = queue.pop()
            visitedSet.add(currentNodeWithDistance.nodeId)
            nodesWithDistances.append(currentNodeWithDistance)
            neighborNodes = self.nodeIdToNeighbors[currentNodeWithDistance.nodeId]
            for neighborId in neighborNodes:
                if neighborId not in visitedSet:
                    neighborNodeWithDistance = NodeWithDistance(neighborId, currentNodeWithDistance.distance + 1)
                    queue.appendleft(neighborNodeWithDistance)
                    visitedSet.add(neighborNodeWithDistance.nodeId)

        return nodesWithDistances






def componentsInGraph(gb):
     pass

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

    l = graph.BFS(notNested[0])
    print(l)




    #result = getNumComponents()
    #print(result)
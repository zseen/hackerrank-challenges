#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
import unittest



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
        #print(self.nodeAndNeighbors)

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
            neighborNodes = self.nodeAndNeighbors[currentNodeWithDistance.nodeId]
            for neighborId in neighborNodes:
                if neighborId not in visitedSet:
                    neighborNodeWithDistance = NodeWithDistance(neighborId, currentNodeWithDistance.distance + 1)
                    queue.appendleft(neighborNodeWithDistance)
        return orderedNodeDistance


    def addNotConnectedNodeDistanceToDistances(self, startNodeId, orderedNodeDistance):
        initialNodesList = list(self.nodeAndNeighbors.keys())

        nodesIdsSet = set([node.nodeId for node in orderedNodeDistance ])


        for item in initialNodesList:
            if item not in nodesIdsSet:
                notConnectedNode = NodeWithDistance(item, -1)
                orderedNodeDistance.append(notConnectedNode)
        return orderedNodeDistance


    def printNodesDistanceOrder(self, startNodeId):
        nodesWithDistances = self.BFS(startNodeId)
        orderedNodeIdWithDistances = self.addNotConnectedNodeDistanceToDistances(startNodeId, nodesWithDistances)

        orderedNodeIdWithDistances.sort(key=lambda obj: obj.nodeId)

        listOfDistances = []
        for item in orderedNodeIdWithDistances:
            if item.nodeId == startNodeId:
                continue
            listOfDistances.append(str(item.distance * 6 if item.distance > 0 else item.distance))
        return listOfDistances

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
        #print(edges)
        startNode = int(input())

        graph = Graph()
        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)

        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
        #print(type(graph.printNodesDistanceOrder(startNode)))

        for item in graph.printNodesDistanceOrder(startNode):
            print(item, end=" ")
        #print(result)




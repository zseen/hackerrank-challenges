#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
import unittest


LOCAL_INPUT = "ON"


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
        orderedNodeDistances = []

        while queue:
            currentNodeWithDistance = queue.pop()
            visitedSet.add(currentNodeWithDistance.nodeId)
            orderedNodeDistances.append(currentNodeWithDistance)
            neighborNodes = self.nodeIdToNeighbors[currentNodeWithDistance.nodeId]
            for neighborId in neighborNodes:
                if neighborId not in visitedSet:
                    neighborNodeWithDistance = NodeWithDistance(neighborId, currentNodeWithDistance.distance + 1)
                    queue.appendleft(neighborNodeWithDistance)
                    visitedSet.add(neighborNodeWithDistance.nodeId)

        return orderedNodeDistances

    def addNotConnectedNodeDistanceToDistances(self, orderedNodeDistances):
        initialNodesList = list(self.nodeIdToNeighbors.keys())

        nodesIdsSet = set([node.nodeId for node in orderedNodeDistances])

        for item in initialNodesList:
            if item not in nodesIdsSet:
                notConnectedNode = NodeWithDistance(item, -1)
                orderedNodeDistances.append(notConnectedNode)
        return orderedNodeDistances

    def printNodesDistanceOrder(self, startNodeId):
        nodesWithDistances = self.BFS(startNodeId)
        orderedNodeIdWithDistances = self.addNotConnectedNodeDistanceToDistances(nodesWithDistances)

        orderedNodeIdWithDistances.sort(key=lambda obj: obj.nodeId)

        listOfDistances = []
        for item in orderedNodeIdWithDistances:
            if item.nodeId == startNodeId:
                continue
            listOfDistances.append(str(item.distance * 6 if item.distance > 0 else item.distance))

        return listOfDistances


def getInputSource():
        nm = input().split()
        nodesNum = int(nm[0])
        edgesNum = int(nm[1])
        edges = []
        for _ in range(edgesNum):
            edges.append(list(map(int, input().rstrip().split())))

        startNode = int(input())

        graph = Graph()
        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)

        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
            graph.addEdge(graphEdges[1], graphEdges[0])
            
        return graph.printNodesDistanceOrder(startNode)


def main():
    if LOCAL_INPUT == "ON":
        sys.stdin = open('BFS_Hackerrank_input.txt')
        q = int(input())

        for q_itr in range(q):
            result = getInputSource()
            for item in result:
                print(item, end=" ")

    elif LOCAL_INPUT == "OFF":
        with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
            q = int(input())

            for q_itr in range(q):
                result = getInputSource()
                fptr.write(' '.join(map(str, result)))
                fptr.write('\n')
    else:
        print("Please set LOCAL_INPUT to 'ON' or 'OFF.")


class TestPrintNodesDistanceOrder(unittest.TestCase):
    def test_printNodesDistanceOrder_startNodeIs1_allNodesConnected_1EdgeLevel(self):
        nodesNum = 3
        startNode = 1
        edges = [[1, 2], [1, 3]]
        graph = Graph()

        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)
        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
        self.assertTrue((graph.printNodesDistanceOrder(startNode) == ['6', '6']))

    def test_printNodesDistanceOrder_startNodeIs1_allNodesConnected_2EdgeLevels(self):
        nodesNum = 4
        startNode = 1
        edges = [[1, 2], [1, 3], [3, 4]]
        graph = Graph()

        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)
        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
        self.assertTrue((graph.printNodesDistanceOrder(startNode) == ['6', '6', '12']))

    def test_printNodesDistanceOrder_startNodeIs2_allNodesConnected_1EdgeLevel(self):
        nodesNum = 3
        startNode = 2
        edges = [[2, 1], [2, 3]]
        graph = Graph()

        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)
        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
            graph.addEdge(graphEdges[1], graphEdges[0])
        self.assertTrue((graph.printNodesDistanceOrder(startNode) == ['6', '6']))

    def test_printNodesDistanceOrder_startNodeIs1_notAllNodesConnected_1EdgeLevel(self):
        nodesNum = 4
        startNode = 1
        edges = [[1, 2], [1, 3]]
        graph = Graph()

        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)
        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
        self.assertTrue((graph.printNodesDistanceOrder(startNode) == ['6', '6', '-1']))

    def test_printNodesDistanceOrder_startNodeIs3_notAllNodesConnected_2EdgeLevels(self):
        nodesNum = 5
        startNode = 3
        edges = [[3, 2], [3, 4], [4, 1]]
        graph = Graph()

        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)
        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
        self.assertTrue((graph.printNodesDistanceOrder(startNode) == ['12', '6', '6', '-1']))

    def test_printNodesDistanceOrder_startNodeIs3_allNodesConnected_3EdgeLevels(self):
        nodesNum = 7
        startNode = 3
        edges = [[1, 2], [3, 1], [2, 4], [2, 5], [3, 5], [3, 6], [3, 7]]
        graph = Graph()

        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)
        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
        self.assertTrue((graph.printNodesDistanceOrder(startNode) == ['6', '12', '18', '6', '6', '6']))

    def test_printNodesDistanceOrder_startNodeIs3_notAllNodesConnected_3EdgeLevels(self):
        nodesNum = 7
        startNode = 3
        edges = [[1, 2], [3, 1], [2, 4], [2, 5], [3, 5], [3, 7]]
        graph = Graph()

        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)
        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
        self.assertTrue((graph.printNodesDistanceOrder(startNode) == ['6', '12', '18', '6', '-1', '6']))

    def test_printNodesDistanceOrder_startNodeIs2_noNodesConnected_0EdgeLevels(self):
        nodesNum = 3
        startNode = 2
        edges = []
        graph = Graph()

        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)
        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
        self.assertTrue((graph.printNodesDistanceOrder(startNode) == ['-1', '-1']))

    def test_printNodesDistanceOrder_startNodeIs1_allNodesConnected_1EdgeLevel_edgesAddedTwiceOriginalOrder(self):
        nodesNum = 3
        startNode = 1
        edges = [[1, 2], [1, 3], [1, 2], [1, 3]]
        graph = Graph()

        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)
        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
        self.assertTrue((graph.printNodesDistanceOrder(startNode) == ['6', '6']))

    def test_printNodesDistanceOrder_startNodeIs1_allNodesConnected_1EdgeLevel_edgesAddedTwiceReversedOrder(self):
        nodesNum = 3
        startNode = 1
        edges = [[1, 2], [1, 3], [3, 1]]
        graph = Graph()

        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)
        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
        self.assertTrue((graph.printNodesDistanceOrder(startNode) == ['6', '6']))

    def test_printNodesDistanceOrder_startNodeIs1_allNodesConnected_2EdgeLevels_squareShapedGraph(self):
        nodesNum = 4
        startNode = 1
        edges = [[1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 1], [1, 4]]
        graph = Graph()

        for nodeId in range(1, nodesNum + 1):
            graph.addNode(nodeId)
        for graphEdges in edges:
            graph.addEdge(graphEdges[0], graphEdges[1])
        self.assertTrue((graph.printNodesDistanceOrder(startNode) == ['6', '12', '6']))





if __name__ == "__main__":
    main()
    #unittest.main()



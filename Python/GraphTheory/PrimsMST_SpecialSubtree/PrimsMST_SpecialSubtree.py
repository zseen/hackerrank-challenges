import math
import os
import random
import re
import sys

# Complete the prims function below.


class Node:
    def __init__(self, nodeId):
        self.nodeId = nodeId

class Edge:
    def __init__(self):
        self.vertexesWithWeight = []
        self.vertexToNeighbors = {}

    def addVertexesWithWeight(self, vertex1, vertex2, weight):
        self.vertexesWithWeight.append([vertex1, vertex2, weight])

    def addNode(self, nodeID):
        self.vertexToNeighbors[nodeID] = set()

    def addEdge(self, startNodeId, endNodeID):
        self.vertexToNeighbors[startNodeId].add(endNodeID)


    def prims(self, nodesNum, edges, startVertex):
        #print(edges)
        visitedVertexes = {}
        allNodesDict = self.vertexToNeighbors.keys()


        while len(visitedVertexes) != nodesNum:


        print(allNodesDict)


if __name__ == '__main__':
    sys.stdin = open("PrimsMST_SpecialSubtree_input.txt")
    nm = input().split()
    nodesNum = int(nm[0])

    edgesNum = int(nm[1])
    edges = []
    for _ in range(edgesNum):
        edges.append(list(map(int, input().rstrip().split())))

    e = Edge()
    allVertexesInEdgesList = []
    for subList in edges:
        allVertexesInEdgesList.extend(subList)


    for nodeId in allVertexesInEdgesList:
        e.addNode(nodeId)

    for edge in edges:
        e.addEdge(edge[0], edge[1])
        e.addEdge(edge[1], edge[0])



    for i in edges:
        e.addVertexesWithWeight(i[0], i[1], i[2])



    #print(edges)
    start = int(input())

    result = e.prims(nodesNum, edges, start)

    print(result)
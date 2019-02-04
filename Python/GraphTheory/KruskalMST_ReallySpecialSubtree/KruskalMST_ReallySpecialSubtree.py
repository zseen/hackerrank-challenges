#KruskalMST_ReallySpecialSubtree.py

#!/bin/python3

import math
import os
import random
import re
import sys


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None


class UnionFind:
    def __init__(self, numSets):
        self.nodeIdToNode = {}
        for i in range(1, numSets + 1):
            self.nodeIdToNode[i] = Node(i)

    def union(self, id1, id2):
        p1 = self.find(id1)
        p2 = self.find(id2)

        p1.parent = p2

    def find(self, id):
        node = self.nodeIdToNode[id]

        potentialParent = node

        while potentialParent.parent is not None:
            potentialParent = potentialParent.parent

        return potentialParent


class Graph:
    def __init__(self):
        self.edgesWithWeight = []
        self.edgeWeight = None
        self.vertex1 = None
        self.vertex2 = None

    def addEdgeWithWeight(self, edgeWithWeight):
        self.edgesWithWeight.append(edgeWithWeight)

    def getEdgeWeight(self, edge):
        self.edgeWeight = edge[2]
        return self.edgeWeight

    def getVertex1(self, edge):
        self.vertex1 = edge[0]
        return self.vertex1

    def getVertex2(self, edge):
        self.vertex2 = edge[1]
        return self.vertex2

    def sortGraphByWeight(self):
        self.edgesWithWeight.sort(key=lambda x:x[2])

if __name__ == '__main__':
    sys.stdin = open("KruskalMST_ReallySpecialSubtree_input.txt")
    g_nodes, g_edges = map(int, input().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    mst = UnionFind(g_nodes)

    graph = Graph()
    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().split())
        graph.addEdgeWithWeight([g_from[i], g_to[i], g_weight[i]])

    graph.sortGraphByWeight()

    minimumCost = 0
    for edge in graph.edgesWithWeight:
        vertex1 = graph.getVertex1(edge)
        vertex2 = graph.getVertex2(edge)
        parent1 = mst.find(vertex1)
        parent2 = mst.find(vertex2)
        if parent1 != parent2:
            x = minimumCost
            minimumCost += graph.getEdgeWeight(edge)
            mst.union(vertex1, vertex2)

    print(minimumCost)



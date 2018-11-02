#!/bin/python3

import os
import sys

#
# Complete the componentsInGraph function below.
#

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


def getNumComponents(numNodes, edges):
    unionfind = UnionFind(numNodes)
    numComponents = numNodes

    for startId, endId in edges:
        if unionfind.find(startId) != unionfind.find(endId):
            unionfind.union(startId, endId)
            numComponents -= 1

    return numComponents






def componentsInGraph(gb):
    #
    # Write your code here.
    pass

if __name__ == '__main__':
    sys.stdin = open("ComponentsInAGraph_input.txt")

    n = int(input())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))


    print(gb)

    #result = getNumComponents()
    #print(result)
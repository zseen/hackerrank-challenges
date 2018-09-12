#!/bin/python3
import unittest
import math
import os
import random
import re
import sys

LOCAL_INPUT = "ON"


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None


class UnionFind:
    def __init__(self, numSets):
        self.nodeIdToNode = {}
        for i in range(1, numSets + 1):
            self.nodeIdToNode[i] = Node(i)

    def union(self, nodeId1, nodeId2):
        p1 = self.findParent(nodeId1)
        p2 = self.findParent(nodeId2)

        p1.parent = p2

    def findParent(self, nodeId):
        node = self.nodeIdToNode[nodeId]

        possibleParent = node

        while possibleParent.parent is not None:
            possibleParent = possibleParent.parent

        return possibleParent


def getComponentsNum(nodesNum, edges):
    uf = UnionFind(nodesNum)
    componentsNum = nodesNum

    for startId, endId in edges:
        if uf.findParent(startId) != uf.findParent(endId):
            uf.union(startId, endId)
            componentsNum -= 1

    return componentsNum


def getMinimalCost(citiesNum, libraryCost, roadCost, roadsBetweenCities):
    communitiesNum = getComponentsNum(citiesNum, roadsBetweenCities)
    minimalRoadsCost = (citiesNum - communitiesNum) * roadCost
    libraryEachCommunityCost = communitiesNum * libraryCost
    return minimalRoadsCost + libraryEachCommunityCost


def parseInputAndReturnMinimalCost():
    nmC_libC_road = input().split()
    citiesNum = int(nmC_libC_road[0])
    roadsNum = int(nmC_libC_road[1])
    libraryCost = int(nmC_libC_road[2])
    roadCost = int(nmC_libC_road[3])
    roadsBetweenCities = []

    for _ in range(roadsNum):
        roadsBetweenCities.append(list(map(int, input().rstrip().split())))

    if libraryCost <= roadCost:
        minimalCost = citiesNum * libraryCost
    else:
        minimalCost = getMinimalCost(citiesNum, libraryCost, roadCost, roadsBetweenCities)
    return minimalCost


def main():
    if LOCAL_INPUT == "ON":
        sys.stdin = open('RoadsAndLibraries_input.txt')
        q = int(input())
        for q_itr in range(q):
            minimalCost = parseInputAndReturnMinimalCost()
            print(minimalCost)
    elif LOCAL_INPUT == "OFF":
        with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
            q = int(input())
            for q_itr in range(q):
                minimalCost = parseInputAndReturnMinimalCost()
                fptr.write(str(minimalCost) + '\n')

    else:
        print("Please set LOCAL_INPUT to 'ON' or 'OFF'.")


class TestUnionFind(unittest.TestCase):
    def test_unionFind_noUnions_findReturnsDifferentNodes(self):
        uf = UnionFind(2)
        self.assertNotEqual(uf.findParent(1), uf.findParent(2))

    def test_unionFind_unionCalled_findReturnsSameNodes(self):
        uf = UnionFind(2)
        uf.union(1, 2)
        self.assertEqual(uf.findParent(1), uf.findParent(2))



if __name__ == '__main__':
    main()
    #unittest.main()



            # Misc: print a linked list

# def printLinkedList(headNode):
#     traversalNode = headNode
#
#     while (traversalNode != None):
#         print(traversalNode.data)
#
#         traversalNode = traversalNode.next
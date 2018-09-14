#!/bin/python3
import os
import sys
import unittest

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


def getMinimalCost(citiesNum, libraryCost, roadCost, roadsBetweenCities):
    if libraryCost <= roadCost:
        minimalCost = citiesNum * libraryCost
    else:
        communitiesNum = getNumComponents(citiesNum, roadsBetweenCities)
        minimalRoadsCost = (citiesNum - communitiesNum) * roadCost
        minLibraryEachCommunityCost = communitiesNum * libraryCost
        minimalCost = minimalRoadsCost + minLibraryEachCommunityCost

    return minimalCost


def parseInputAndReturnMinimalCost():
    nmC_libC_road = input().split()
    citiesNum = int(nmC_libC_road[0])
    roadsNum = int(nmC_libC_road[1])
    libraryCost = int(nmC_libC_road[2])
    roadCost = int(nmC_libC_road[3])
    roadsBetweenCities = []

    for _ in range(roadsNum):
        roadsBetweenCities.append(list(map(int, input().rstrip().split())))

    minCost = getMinimalCost(citiesNum, libraryCost, roadCost, roadsBetweenCities)
    return minCost


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
    def test_unionFind_noUnions_findReturnsDifferentSets(self):
        uf = UnionFind(2)
        self.assertNotEqual(uf.find(1), uf.find(2))

    def test_unionFind_unionCalled_findReturnsSameSet(self):
        uf = UnionFind(2)
        uf.union(1, 2)
        self.assertEqual(uf.find(1), uf.find(2))

    def test_unionFind_unionCalledButNotDirectly_findReturnsSameSet(self):
        numNodes = 3
        uf = UnionFind(numNodes)
        uf.union(1, 2)
        uf.union(2, 3)
        self.assertEqual(uf.find(1), uf.find(3))




if __name__ == '__main__':
    # main()
    unittest.main()


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


LOCAL_INPUT = "ON"


class CitiesAndRoads:
    def __init__(self):
        self.nodesToEdges = {}

    def addNode(self, nodeId):
        self.nodesToEdges[nodeId] = set()

    def addEdge(self, startNodeId, endNodeId):
        self.nodesToEdges[startNodeId].add(endNodeId)

    def visitConnectableNodes(self, startNodeId):
        nodesToVisit = deque()

        nodesToVisit.appendleft(startNodeId)
        visitedNodes = set()

        while nodesToVisit:
            currentNode = nodesToVisit.pop()
            visitedNodes.add(currentNode)

            neighborNodes = self.nodesToEdges[currentNode]
            for neighborNode in neighborNodes:
                if neighborNode not in visitedNodes:
                    nodesToVisit.appendleft(neighborNode)
                    visitedNodes.add(neighborNode)

        return visitedNodes

    def countGroupsOfConnectableNodes(self, startNodeId):
        unvisitedSet = set(self.nodesToEdges.keys())
        componentsCounter = 0
        while unvisitedSet:
            currentVisitedNodesList = list(self.visitConnectableNodes(next(iter(unvisitedSet))))
            for node in currentVisitedNodesList:
                unvisitedSet.remove(node)
            componentsCounter += 1
        return componentsCounter

    def getMinimumCostBuildingRoads(self, citiesNum, libraryCost, roadCost, startCity):
        communitiesNum = self.countGroupsOfConnectableNodes(startCity)
        minimalRoadsCost = (citiesNum - communitiesNum) * roadCost
        libraryEachCommunityCost = communitiesNum * libraryCost
        return minimalRoadsCost + libraryEachCommunityCost


def createPossibleRoadsMap(roadsNum, citiesNum):
    roadsBetweenCities = []
    for _ in range(roadsNum):
        roadsBetweenCities.append(list(map(int, input().rstrip().split())))

    citiesWithRoads = CitiesAndRoads()
    for city in range(1, citiesNum + 1):
        citiesWithRoads.addNode(city)

    for road in roadsBetweenCities:
        citiesWithRoads.addEdge(road[0], road[1])
        citiesWithRoads.addEdge(road[1], road[0])
    return citiesWithRoads


def parseInputAndCompareCost():
    nmC_libC_road = input().split()
    citiesNum = int(nmC_libC_road[0])
    roadsNum = int(nmC_libC_road[1])
    libraryCost = int(nmC_libC_road[2])
    roadCost = int(nmC_libC_road[3])
    citiesWithRoads = createPossibleRoadsMap(roadsNum, citiesNum)
    startCity = 1
    if libraryCost <= roadCost:
        minimalCost = citiesNum * libraryCost
    else:
        minimalCost = citiesWithRoads.getMinimumCostBuildingRoads(citiesNum, libraryCost, roadCost, startCity)
    return minimalCost



def main():
    if LOCAL_INPUT == "ON":
        sys.stdin = open('RoadsAndLibraries_input.txt')
        q = int(input())
        for q_itr in range(q):
            minimalCost = parseInputAndCompareCost()
            print(minimalCost)

    elif LOCAL_INPUT == "OFF":
        with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
            q = int(input())
            for q_itr in range(q):
                minimalCost = parseInputAndCompareCost()
                fptr.write(str(minimalCost) + '\n')

    else:
        print("Please set LOCAL_INPUT to 'ON' or 'OFF'.")


if __name__ == '__main__':
    main()


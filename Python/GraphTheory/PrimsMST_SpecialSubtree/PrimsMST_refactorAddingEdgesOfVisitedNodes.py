import sys
import time


class Edge:
    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.nodeToEdges = {}
        self.candidateEdgesSet = set()

    def addEdgeToGraph(self, edge):
        if edge.startVertex not in self.nodeToEdges:
            self.nodeToEdges[edge.startVertex] = []
        if edge.endVertex not in self.nodeToEdges:
            self.nodeToEdges[edge.endVertex] = []
        self.nodeToEdges[edge.startVertex].append(edge)
        self.nodeToEdges[edge.endVertex].append(edge)

    def addEdgesToCandidateEdgesSet(self, visitedNodesSet, nodeMostRecentlyVisited):
        edgesFromMostRecentlyVisitedNode = self.nodeToEdges[nodeMostRecentlyVisited]
        for edge in edgesFromMostRecentlyVisitedNode:
            if edge.endVertex not in visitedNodesSet or edge.startVertex not in visitedNodesSet:
                self.candidateEdgesSet.add(edge)
            elif edge in self.candidateEdgesSet:
                self.candidateEdgesSet.remove(edge)

    def getEdgeWithMinimumWeight(self):
        bestEdge = Edge(None, None, sys.maxsize)
        for edge in self.candidateEdgesSet:
            if edge.weight < bestEdge.weight:
                    bestEdge = edge

        return bestEdge


def getMST(nodesNum, graph, startNode):
    visitedNodesSet = {startNode}
    minimumWeightTotal = 0
    nodeMostRecentlyVisited = startNode

    while len(visitedNodesSet) != nodesNum:
        graph.addEdgesToCandidateEdgesSet(visitedNodesSet, nodeMostRecentlyVisited)

        bestEdge = graph.getEdgeWithMinimumWeight()
        minimumWeightTotal += bestEdge.weight

        if bestEdge.startVertex not in visitedNodesSet:
            nodeMostRecentlyVisited = bestEdge.startVertex
        else:
            nodeMostRecentlyVisited = bestEdge.endVertex

        visitedNodesSet.add(nodeMostRecentlyVisited)

    return minimumWeightTotal


def solvePrimsMST():
    sys.stdin = open("PrimsMST_SpecialSubtree_input.txt")

    nm = input().split()
    nodesNum = int(nm[0])
    edgesNum = int(nm[1])
    edges = []
    graph = Graph()

    for _ in range(edgesNum):
        edges.append(list(map(int, input().rstrip().split())))

    for edge in edges:
        startVertex, endVertex, weight = edge[0], edge[1], edge[2]
        e = Edge(startVertex, endVertex, weight)
        graph.addEdgeToGraph(e)

    startNode = int(input())

    return getMST(nodesNum, graph, startNode)


def main():
    runTimes = []
    testRange = 30
    for test in range(testRange):
        start = time.clock()

        minimumWeightMST = solvePrimsMST()

        end = time.clock()
        runTimes.append(end - start)

    print(round(sum(runTimes) / testRange, 2))

if __name__ == '__main__':
    main()


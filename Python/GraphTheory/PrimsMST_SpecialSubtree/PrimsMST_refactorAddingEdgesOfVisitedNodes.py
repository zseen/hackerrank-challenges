import sys
import time


class Edge:
    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.edges = {}

    def addEdgeToGraph(self, edge):
        if edge.startVertex not in self.edges:
            self.edges[edge.startVertex] = []
        if edge.endVertex not in self.edges:
            self.edges[edge.endVertex] = []
        self.edges[edge.startVertex].append(edge)
        self.edges[edge.endVertex].append(edge)

    def getEdgesForSubgraphWithNodes(self, nodesContainer, edgesAlreadyAddedSet):
        for startNode, edgesFromStartNode in self.edges.items():
            if startNode in nodesContainer:
                for edge in edgesFromStartNode:
                    if edge.endVertex not in nodesContainer or edge.startVertex not in nodesContainer:
                        edgesAlreadyAddedSet.add(edge)
                    elif edge in edgesAlreadyAddedSet:
                        edgesAlreadyAddedSet.remove(edge)

        return edgesAlreadyAddedSet


def getEdgeWithMinimumWeight(edges, visitedNodes):
    bestEdge = Edge(None, None, sys.maxsize)
    for edge in edges:
        if edge.weight < bestEdge.weight:
                bestEdge = edge

    return bestEdge


def getMST(nodesNum, graph, startNode):
    visitedNodesSet = {startNode}
    minimumWeightTotal = 0
    potentialEdges = set()

    while len(visitedNodesSet) != nodesNum:
        edgesFromVisitedNodes = graph.getEdgesForSubgraphWithNodes(visitedNodesSet, potentialEdges)

        bestEdge = getEdgeWithMinimumWeight(edgesFromVisitedNodes, visitedNodesSet)
        minimumWeightTotal += bestEdge.weight

        visitedNodesSet.add(bestEdge.startVertex)
        visitedNodesSet.add(bestEdge.endVertex)

    return minimumWeightTotal


def parseInputAndReturnMinimumWeight():
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
    minimumWeightMST = parseInputAndReturnMinimumWeight()


runTimes = []
testRange = 2
for test in range(testRange):
    start = time.clock()

    if __name__ == '__main__':
        main()

    end = time.clock()
    runTimes.append(end - start)

print(sum(runTimes) / testRange)

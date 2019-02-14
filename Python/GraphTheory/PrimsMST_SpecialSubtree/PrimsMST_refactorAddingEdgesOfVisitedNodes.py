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
        self.candidateEdgesSet = set()

    def addEdgeToGraph(self, edge):
        if edge.startVertex not in self.edges:
            self.edges[edge.startVertex] = []
        if edge.endVertex not in self.edges:
            self.edges[edge.endVertex] = []
        self.edges[edge.startVertex].append(edge)
        self.edges[edge.endVertex].append(edge)

    def addEdgesToCandidateEdgesSet(self, visitedNodesSet):
        for startNode, edgesFromStartNode in self.edges.items():
            if startNode in visitedNodesSet:
                for edge in edgesFromStartNode:
                    if edge.endVertex not in visitedNodesSet or edge.startVertex not in visitedNodesSet:
                        self.candidateEdgesSet.add(edge)
                    elif edge in self.candidateEdgesSet:
                        self.candidateEdgesSet.remove(edge)

    def getCandidateEdges(self):
        return self.candidateEdgesSet


def getEdgeWithMinimumWeight(edges, visitedNodes):
    bestEdge = Edge(None, None, sys.maxsize)
    for edge in edges:
        if edge.weight < bestEdge.weight:
                bestEdge = edge

    return bestEdge


def getMST(nodesNum, graph, startNode):
    visitedNodesSet = {startNode}
    minimumWeightTotal = 0

    while len(visitedNodesSet) != nodesNum:
        graph.addEdgesToCandidateEdgesSet(visitedNodesSet)
        edgesFromVisitedNodes = graph.getCandidateEdges()

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
testRange = 1
for test in range(testRange):
    start = time.clock()

    if __name__ == '__main__':
        main()

    end = time.clock()
    runTimes.append(end - start)

print(sum(runTimes) / testRange)

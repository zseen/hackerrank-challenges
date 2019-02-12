import sys


class Edge:
    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight


def getEdgesListFromGraph(graph, nodesContainer):
    edgesList = []
    for key, value in graph.items():
        if key in nodesContainer:
            for edge in value:
                edgesList.append(edge)
    return edgesList


def removeEdgeFromGraph(graph, edge):
    graph[edge.startVertex].remove(edge)
    graph[edge.endVertex].remove(edge)


def addEdgeVerticesToSet(nodesSet, edge):
    nodesSet.add(edge.startVertex)
    nodesSet.add(edge.endVertex)


def getEdgeWithMinimumWeight(edges, visitedNodes, currentMinWeight):
    bestEdge = None
    for edge in edges:
        currStart = edge.startVertex
        currEnd = edge.endVertex
        currEdgeWeight = edge.weight
        isOneNodeNotVisited = currStart not in visitedNodes or currEnd not in visitedNodes
        if isOneNodeNotVisited and currEdgeWeight < currentMinWeight:
            currentMinWeight = currEdgeWeight
            bestEdge = edge

    return bestEdge


def getMST(nodesNum, graph, startNode):
    visitedNodesSet = {startNode}
    minimumWeightTotal = 0

    while len(visitedNodesSet) != nodesNum:
        largestPossibleWeight = sys.maxsize
        edgesFromVisitedNodes = getEdgesListFromGraph(graph, visitedNodesSet)

        bestEdge = getEdgeWithMinimumWeight(edgesFromVisitedNodes, visitedNodesSet, largestPossibleWeight)
        minimumWeightTotal += bestEdge.weight

        addEdgeVerticesToSet(visitedNodesSet, bestEdge)
        removeEdgeFromGraph(graph, bestEdge)

    return minimumWeightTotal


def main():
    sys.stdin = open("PrimsMST_SpecialSubtree_input.txt")

    nm = input().split()
    nodesNum = int(nm[0])
    edgesNum = int(nm[1])
    edges = []
    graph = {}

    for _ in range(edgesNum):
        edges.append(list(map(int, input().rstrip().split())))

    for edge in edges:
        startVertex, endVertex, weight = edge[0], edge[1], edge[2]
        e = Edge(startVertex, endVertex, weight)
        if e.startVertex not in graph:
            graph[e.startVertex] = []
        if e.endVertex not in graph:
            graph[e.endVertex] = []
        graph[e.startVertex].append(e)
        graph[e.endVertex].append(e)

    startNode = int(input())

    result = getMST(nodesNum, graph, startNode)
    print(result)

if __name__ == '__main__':
    main()

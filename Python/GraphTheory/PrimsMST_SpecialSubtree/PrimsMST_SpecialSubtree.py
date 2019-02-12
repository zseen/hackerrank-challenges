import sys


class Edge:
    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight


def getEdgesForSubgraphWithNodes(graph, nodesContainer):
    edgesList = []
    for startNode, edges in graph.items():
        if startNode in nodesContainer:
            for edge in edges:
                edgesList.append(edge)
    return edgesList


def getEdgeWithMinimumWeight(edges, visitedNodes):
    bestEdge = Edge(None, None, sys.maxsize)
    for edge in edges:
        isOneNodeNotVisited = edge.startVertex not in visitedNodes or edge.endVertex not in visitedNodes
        if isOneNodeNotVisited and edge.weight < bestEdge.weight:
                bestEdge = edge

    return bestEdge


def getMST(nodesNum, graph, startNode):
    visitedNodesSet = {startNode}
    minimumWeightTotal = 0

    while len(visitedNodesSet) != nodesNum:
        edgesFromVisitedNodes = getEdgesForSubgraphWithNodes(graph, visitedNodesSet)

        bestEdge = getEdgeWithMinimumWeight(edgesFromVisitedNodes, visitedNodesSet)
        minimumWeightTotal += bestEdge.weight

        visitedNodesSet.add(bestEdge.startVertex)
        visitedNodesSet.add(bestEdge.endVertex)


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

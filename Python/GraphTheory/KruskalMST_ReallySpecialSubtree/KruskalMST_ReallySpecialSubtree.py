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


class Edge:
    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight


def getMinimumWeight(edgesList):
    allNodes = set()
    for e in edgesList:
        allNodes.add(e.startVertex)
        allNodes.add(e.endVertex)

    componentLookup = UnionFind(len(allNodes))
    edgesList.sort(key=lambda e: e.weight)
    
    minimumWeightTotal = 0
    for edge in edgesList:
        parent1 = componentLookup.find(edge.startVertex)
        parent2 = componentLookup.find(edge.endVertex)
        if parent1 != parent2:
            minimumWeightTotal += edge.weight
            componentLookup.union(edge.startVertex, edge.endVertex)

    return minimumWeightTotal


def main():
    sys.stdin = open("KruskalMST_ReallySpecialSubtree_input.txt")
    g_nodes, g_edges = map(int, input().split())
    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    edgesList = []
    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().split())
        edge = Edge(g_from[i], g_to[i], g_weight[i])
        edgesList.append(edge)

    minimumWeight = getMinimumWeight(edgesList)
    print(minimumWeight)


if __name__ == '__main__':
    main()

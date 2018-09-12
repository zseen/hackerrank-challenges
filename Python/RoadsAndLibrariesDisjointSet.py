import unittest


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
        p1 = self.find(nodeId1)
        p2 = self.find(nodeId2)

        p1.parent = p2

    def find(self, nodeId):
        node = self.nodeIdToNode[nodeId]

        parentCandidate = node

        while parentCandidate.parent is not None:
            parentCandidate = parentCandidate.parent

        return parentCandidate


def main():
    numNodes = 5
    edges = [(1,2), (2,3), (3,4), (4, 2), (4, 1)]

    uf = UnionFind(numNodes)
    numComponents = numNodes

    for startId, endId in edges:
        if uf.find(startId) != uf.find(endId):
            uf.union(startId, endId)
            numComponents -= 1

    print(numComponents)


class TestUnionFind(unittest.TestCase):
    def test_unionFind_noUnions_findReturnsDifferentNodes(self):
        uf = UnionFind(2)
        self.assertNotEqual(uf.find(1), uf.find(2))

    def test_unionFind_unionCalled_findReturnsSameNodes(self):
        uf = UnionFind(2)
        uf.union(1, 2)
        self.assertEqual(uf.find(1), uf.find(2))



if __name__ == '__main__':
    #main()
    unittest.main()



            # Misc: print a linked list

# def printLinkedList(headNode):
#     traversalNode = headNode
#
#     while (traversalNode != None):
#         print(traversalNode.data)
#
#         traversalNode = traversalNode.next
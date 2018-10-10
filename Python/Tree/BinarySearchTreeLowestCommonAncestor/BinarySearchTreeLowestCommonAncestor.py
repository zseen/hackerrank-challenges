from Library.Tree import BinarySearchTree
from collections import deque


def findPath(root, node, path):
    if root:
        if root.value == node:
            path.appendleft(root)
        else:
            if findPath(root.left, node, path):
                path.appendleft(root)
            elif findPath(root.right, node, path):
                path.appendleft(root)
    return path


def orderPathFromRootToNode(root, node):
    route = deque()
    pathOrder = findPath(root, node, route)
    return pathOrder


def lca(root, v1, v2):
    if root:
        firstNodePath = orderPathFromRootToNode(root, v1)
        secondNodePath = orderPathFromRootToNode(root, v2)

        lowCommAnc = None
        for value1, value2 in zip(firstNodePath, secondNodePath):
            if value1 == value2:
                lowCommAnc = value1

        return lowCommAnc


tree = BinarySearchTree.BinarySearchTree()
nodesList = list((7, 5, 1, 3, 2, 6, 8, 4, 9))

for i in range(0, len(nodesList)):
    tree.insert(nodesList[i])
lowestCommonAncestor = lca(tree.root, 3, 4)
print(lowestCommonAncestor.value)


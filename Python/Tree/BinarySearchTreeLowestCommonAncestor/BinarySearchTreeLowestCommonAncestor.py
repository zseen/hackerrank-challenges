from Library.Tree import BinarySearchTree

tree = BinarySearchTree.BinarySearchTree()
nodesList = list((7, 5, 1, 3, 2, 6, 8, 4, 9))

for i in range(0, len(nodesList)):
    tree.insert(nodesList[i])


def findPath(root, node, path):
    if root:
        if root.value == node:
            path.append(root)
        else:
            if findPath(root.left, node, path):
                path.append(root)
            elif findPath(root.right, node, path):
                path.append(root)
    return path


def orderPathFromRootToNode(root, node):
    route = []
    pathOrder = list(reversed(findPath(root, node, route)))
    return pathOrder


def lca(root, v1, v2):
    if root:
        firstNodePath = orderPathFromRootToNode(root, v1)
        secondNodePath = orderPathFromRootToNode(root, v2)

        for index in range(0, min(len(firstNodePath), len(secondNodePath))):
            if firstNodePath[index] != secondNodePath[index]:
                return firstNodePath[index-1]

        return firstNodePath[-1] if len(firstNodePath) < len(secondNodePath) else secondNodePath[-1]


lowestCommonAncestor = lca(tree.root, 5, 2)
print(lowestCommonAncestor.value)


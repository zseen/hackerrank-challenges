from Library.Tree import BinarySearchTree


def check(root, visitedNodesValues):
    if root:
        check(root.left, visitedNodesValues)
        visitedNodesValues.append(root.value)
        check(root.right, visitedNodesValues)


def getCheckIfBSTResult(tree, initialNodesNum):
    inorderNodeValues = []

    check(tree.root, inorderNodeValues)

    for i in range(0, len(inorderNodeValues) - 1):
        if inorderNodeValues[i] > inorderNodeValues[i + 1] or len(inorderNodeValues) != initialNodesNum:
            return False
    return True


def main():
    tree = BinarySearchTree.BinarySearchTree()
    nodesList = [4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 16, 16]
    initialNodesNum = len(nodesList)

    for node in range(len(nodesList)):
        tree.insert(nodesList[node])

    isBST = getCheckIfBSTResult(tree, initialNodesNum)
    print(isBST)

if __name__ == "__main__":
    main()

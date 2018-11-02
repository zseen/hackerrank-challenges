from Library.Tree import BinarySearchTree


def check(root, visitedNodesValues):
    if root:
        check(root.left, visitedNodesValues)
        visitedNodesValues.append(root.value)
        check(root.right, visitedNodesValues)


def getCheckIfBSTResult(tree):
    inorderNodeValues = []

    check(tree.root, inorderNodeValues)

    for i in range(0, len(inorderNodeValues) - 1):
        if inorderNodeValues[i] > inorderNodeValues[i + 1]:
            return False
    return True


def main():
    nodesList = [4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 16, 16]

    if len(nodesList) == len(set(nodesList)):
        tree = BinarySearchTree.BinarySearchTree()

        for node in range(len(nodesList)):
            tree.insert(nodesList[node])

        isBST = getCheckIfBSTResult(tree)
        print("Yes" if isBST else "No")

    else:
        print("No")

if __name__ == "__main__":
    main()

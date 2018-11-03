class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def checkTreeWithInorderTraversal(root, visitedNodesValues):
    if root:
        checkTreeWithInorderTraversal(root.left, visitedNodesValues)
        visitedNodesValues.append(root.value)
        checkTreeWithInorderTraversal(root.right, visitedNodesValues)


def getCheckIfBSTResult(root):
    inorderNodeValues = []

    checkTreeWithInorderTraversal(root, inorderNodeValues)

    for i in range(0, len(inorderNodeValues) - 1):
        if inorderNodeValues[i] > inorderNodeValues[i + 1]:
            return False
    return True


def main():
    root = Node(10)
    root.right = Node(1)

    root.left = Node(2)

    isBST = getCheckIfBSTResult(root)
    print("Yes" if isBST else "No")

if __name__ == "__main__":
    main()



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert(value)



def check(root, visitedNodesValues):
    if root:
        check(root.left, visitedNodesValues)
        visitedNodesValues.append(root.value)
        check(root.right, visitedNodesValues)


def getCheckIfBSTResult(root):
    inorderNodeValues = []

    check(root, inorderNodeValues)

    for i in range(0, len(inorderNodeValues) - 1):
        if inorderNodeValues[i] > inorderNodeValues[i + 1]:
            return False
    return True


def main():
    #nodesList = [4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 16, 16]

    tree = Tree()

    root = Node(10)
    root.right = Node(15)

    root.left = Node(2)

    #for node in range(len(nodesList)):
        #tree.insert(nodesList[node])

    isBST = getCheckIfBSTResult(root)
    print("Yes" if isBST else "No")



if __name__ == "__main__":
    main()

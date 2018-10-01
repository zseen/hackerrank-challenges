class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, currentNode):
        if currentNode.value > value:
            if currentNode.left is None:
                currentNode.left = Node(value)
            else:
                self._insert(value, currentNode.left)

        elif currentNode.value < value:
            if currentNode.right is None:
                currentNode.right = Node(value)
            else:
                self._insert(value, currentNode.right)

        else:
            print("Node already in tree.")

    def printTree(self):
        if self.root:
            self._printTree(self.root)

    def _printTree(self, node):

        if node:
            self._printTree(node.left)
            print(str(node.value))
            self._printTree(node.right)

tree = BinarySearchTree()


nodesList = list(input)


for i in range(0, len(nodesList)):
    tree.insert(nodesList[i])






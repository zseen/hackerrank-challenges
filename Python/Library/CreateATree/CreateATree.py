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



    def printInorder(self):
        if self.root:
            self._printInorder(self.root)

    def printPreorder(self):
        if self.root:
            self._printPreorder(self.root)

    def printPostorder(self):
        if self.root:
            self._printPostorder(self.root)

    def _printInorder(self, node):
        if node:
            self._printInorder(node.left)
            print(str(node.value))
            self._printInorder(node.right)

    def _printPreorder(self, node):
        if node:
            print(str(node.value))
            self._printPreorder(node.left)
            self._printPreorder(node.right)

    def _printPostorder(self, node):
        if node:
            self._printPostorder(node.left)
            self._printPostorder(node.right)
            print(str(node.value))

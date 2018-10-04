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


    def _printInorder(self, node, level):
        if node:
            self._printInorder(node.left, level + 1)
            print('  ' * level + str(node.value))
            self._printInorder(node.right, level + 1)

    def printInorder(self):
        level = 0
        if self.root:
            self._printInorder(self.root, level)

    def _printPreorder(self, node, level):
        if node:
            print('  ' * level + str(node.value))
            self._printPreorder(node.left, level + 1)
            self._printPreorder(node.right, level + 1)

    def printPreorder(self):
        level = 0
        if self.root:
            self._printPreorder(self.root, level)

    def _printPostorder(self, node, level):
        if node:
            self._printPostorder(node.left, level + 1)
            self._printPostorder(node.right, level + 1)
            print('  ' * level + str(node.value))

    def printPostorder(self):
        level = 0
        if self.root:
            self._printPostorder(self.root, level)

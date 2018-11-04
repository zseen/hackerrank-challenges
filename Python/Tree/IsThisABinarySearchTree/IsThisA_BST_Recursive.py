import sys

MIN_INT = - sys.maxsize - 1
MAX_INT = sys.maxsize


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def checkIfBST(node, smallestNum, biggestNum):
    if node is None:
        return True

    if node.value <= smallestNum or node.value >= biggestNum:
        return False

    return (checkIfBST(node.left, smallestNum, node.value) and
            checkIfBST(node.right, node.value, biggestNum))


def returnCheckIfBST(node):
    return checkIfBST(node, MIN_INT, MAX_INT)


def main():
    root = Node(10)
    root.right = Node(12)
    root.left = Node(2)

    if checkIfBST(root, MIN_INT, MAX_INT):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()

import sys

MIN_INT = - sys.maxsize - 1
MAX_INT = sys.maxsize


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def checkRecursively(node, smallestNum, biggestNum):
    if node is None:
        return True

    if node.value <= smallestNum or node.value >= biggestNum:
        return False

    return (checkRecursively(node.left, smallestNum, node.value) and
            checkRecursively(node.right, node.value, biggestNum))


def getResultBST(node):
    return checkRecursively(node, MIN_INT, MAX_INT)


def main():
    root = Node(10)
    root.right = Node(12)
    root.left = Node(2)

    if getResultBST(root):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()

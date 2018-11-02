from Library.Tree import BinarySearchTree
import sys

MIN_INT = - sys.maxsize - 1
MAX_INT = sys.maxsize


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
    nodesList = [4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 16, 16]

    tree = BinarySearchTree.BinarySearchTree()
    for node in range(len(nodesList)):
        tree.insert(nodesList[node])

    if not checkIfBST(tree.root, MIN_INT, MAX_INT) or len(nodesList) != len(set(nodesList)):
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()

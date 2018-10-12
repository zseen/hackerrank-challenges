from Library.Tree import BinarySearchTree
from collections import deque


def getLevelOrder(root, visitedNodesValuesList):
    leavesToVisit = deque()
    if root:
        leavesToVisit.append(root)
        while leavesToVisit:
            leaf = leavesToVisit.pop()
            visitedNodesValuesList.append(leaf.value)
            if leaf.left:
                leavesToVisit.appendleft(leaf.left)
            if leaf.right:
                leavesToVisit.appendleft(leaf.right)


def levelOrder(root):
    values = []
    getLevelOrder(root, values)
    for value in values:
        print(value, end=" ")



def main():
    tree = BinarySearchTree.BinarySearchTree()

    nodesList = list((4, 5, 1, 3, 2))
    for i in range(0, len(nodesList)):
        tree.insert(nodesList[i])

    levelOrder(tree.root)



if __name__ == "__main__":
    main()
    
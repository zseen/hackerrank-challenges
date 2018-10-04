from Library.Tree import BinarySearchTree
from collections import deque


def levelOrder(root):
    leavesToVisit = deque()
    if root:
        leavesToVisit.append(root)
        while leavesToVisit:
            leaf = leavesToVisit.pop()
            print(leaf.value, end=' ')
            if leaf.left:
                leavesToVisit.appendleft(leaf.left)
            if leaf.right:
                leavesToVisit.appendleft(leaf.right)


def main():
    tree = BinarySearchTree.BinarySearchTree()

    nodesList = list((4, 5, 1, 3, 2))
    for i in range(0, len(nodesList)):
        tree.insert(nodesList[i])

    levelOrder(tree.root)



if __name__ == "__main__":
    main()
    
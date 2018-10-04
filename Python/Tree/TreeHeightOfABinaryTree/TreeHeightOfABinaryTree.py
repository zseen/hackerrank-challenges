from Library.Tree import BinarySearchTree


def height(root):
    if root:
        leftHeight = height(root.left)
        rightHeight = height(root.right)
        return 1 + max(leftHeight, rightHeight)
    else:
        return -1


tree = BinarySearchTree.BinarySearchTree()
nodesList = list((4, 5, 1, 3, 2))

for i in range(0, len(nodesList)):
    tree.insert(nodesList[i])

treeHeight = height(tree.root)
print(treeHeight)

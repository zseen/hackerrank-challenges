from Library.Tree import BinarySearchTree


def lca(root, v1, v2):
    if v1 < root.value and v2 < root.value:
        return lca(root.left, v1, v2)
    elif v1 > root.value and v2 > root.value:
        return lca(root.right, v1, v2)
    else:
        return root


tree = BinarySearchTree.BinarySearchTree()
nodesList = list((7, 5, 1, 3, 2, 6, 8, 4, 9))

for i in range(0, len(nodesList)):
    tree.insert(nodesList[i])

lowestCommonAncestor = lca(tree.root, 4, 9)
print(lowestCommonAncestor.value)

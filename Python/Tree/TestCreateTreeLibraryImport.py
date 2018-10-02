from Library.CreateATree import CreateATree

tree = CreateATree.BinarySearchTree()
nodesList = list((4, 5, 1, 3, 2))

for i in range(0, len(nodesList)):
    tree.insert(nodesList[i])

#tree.printInorder()
tree.printPreorder()
#tree.printPostorder()


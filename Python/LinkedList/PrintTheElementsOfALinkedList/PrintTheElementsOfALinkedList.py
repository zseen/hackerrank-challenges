import sys


class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        newNode = Node()
        newNode.data = data

        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode

        self.tail = newNode

    def printList(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


def main():
    sys.stdin = open('PrintTheElementsOfALinkedList_input.txt')
    nodesNum = int(input())

    linkedList = LinkedList()

    for _ in range(nodesNum):
        item = int(input())
        linkedList.addNode(item)

    linkedList.printList()


if __name__ == "__main__":
    main()


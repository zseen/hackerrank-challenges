#!/bin/python3

import sys


class Node:
    def __init__(self):
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, string):
        currentNode = self.root

        for char in string:
            if not currentNode.children.get(char):
                currentNode.children[char] = Node()

            currentNode = currentNode.children[char]
            currentNode.count += 1

    def find(self, string):
        currentNode = self.root

        for char in string:
            if not currentNode.children.get(char):
                currentNodeCount = 0
                return currentNodeCount

            currentNode = currentNode.children[char]

        return currentNode.count


def main():
    sys.stdin = open("Contacts_input.txt")

    queries_rows = int(input())
    trie = Trie()

    for i in range(queries_rows):
        query = input().split()
        if query[0] == 'add':
            trie.add(query[1])
        elif query[0] == 'find':
            print(trie.find(query[1]))

if __name__ == '__main__':
    main()
    
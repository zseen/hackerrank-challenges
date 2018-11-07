import sys


class QueueWithTwoStacks:
    def __init__(self):
        self.appendingStack = []
        self.poppingStack = []

    def enqueue(self, item):
        self.appendingStack.append(item)

    def moveItemsFromAppendingToPoppingStackIfEmpty(self):
        if not self.poppingStack:
            while self.appendingStack:
                self.poppingStack.append(self.appendingStack.pop())
        return self.poppingStack

    def dequeue(self):
        self.moveItemsFromAppendingToPoppingStackIfEmpty()
        self.poppingStack.pop()

    def printFirstItemInQueue(self):
        self.moveItemsFromAppendingToPoppingStackIfEmpty()
        print(self.poppingStack[-1])


def main():
    sys.stdin = open("QueueUsingTwoStacks_input.txt")
    queue = QueueWithTwoStacks()

    n = int(input())
    for _ in range(n):
        command = list(map(int, (input().split(' '))))
        if command[0] == 1:
            queue.enqueue(command[1])
        elif command[0] == 2:
            queue.dequeue()
        else:
            queue.printFirstItemInQueue()


if __name__ == '__main__':
    main()

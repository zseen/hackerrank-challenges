import sys


class QueueWithTwoStacks:
    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def enqueue(self, item):
        self.pushStack.append(item)

    def preparePopStack(self):
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())

    def dequeue(self):
        self.preparePopStack()
        self.popStack.pop()

    def printFirstItemInQueue(self):
        self.preparePopStack()
        print(self.popStack[-1])


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

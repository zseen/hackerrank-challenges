import sys


class QueueWithTwoStacks:
    def __init__(self):
        self.appendingStack = []
        self.poppingStack = []
        self.whatToAppend = None


    def mak

    def enqueue_appendToRear(self):
        self.appendingStack.append(self.whatToAppend)

    def dequeue_popFromFront(self):
        self.poppingStack.pop(0)

    def printFirstItemInQueue(self):
        
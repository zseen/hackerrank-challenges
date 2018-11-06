import sys

class Stack:
    def __init__(self):
        self.string = ""
        self.stack = []

    def appendString(self, ending):
        self.string += str(ending)
        self.stack.append(self.string)
        #return self.string

    def deleteEnd(self, charsNumToChop):
        self.string = self.string[:-charsNumToChop]
        self.stack.append(self.string)
        #return self.string

    def printRequestedChar(self, charToPrint):
        print(self.string[charToPrint])
        #return self.string


    def undo(self):
        self.stack.pop()
        self.string = self.stack[-1]
        #return self.string

    def printString(self):
        print(self.string)


def main():
    sys.stdin = open("SimpleTextEditor_input.txt")

    string = Stack()





    n = int(input().strip())

    for _ in range(n):
        x = input().split()
        if x[0] == '1':
            string.appendString(x[1])
            #string.printString()
        elif x[0] == '2':
            string.deleteEnd(int(x[1]))
            #string.printString()
        elif x[0] == '3':
            string.printRequestedChar(int(x[1]) - 1)
            #string.printString()
        elif x[0] == '4':
            string.undo()
            #string.printString()




if __name__ == "__main__":
    main()


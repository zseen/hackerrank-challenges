import sys


class TextEditor:
    def __init__(self):
        self.stringInListForm = []
        self.stack = [self.stringInListForm]
        self.index = 0

    def appendString(self, ending):
        self.stack.append(self.stringInListForm + list(ending))
        self.index += 1
        self.stringInListForm = self.stack[self.index]

    def deleteFromEnd(self, charsNumToChop):
        self.stack.append(self.stringInListForm[:-charsNumToChop])
        self.index += 1
        self.stringInListForm = self.stack[self.index]

    def printRequestedChar(self, charToPrintIndex):
        if len(self.stringInListForm) >= charToPrintIndex:
            print(self.stringInListForm[charToPrintIndex - 1])
        else:
            print("String is shorter than " + str(charToPrintIndex) + " characters.")

    def undoLastModification(self):
        self.stack.pop()
        self.index -= 1
        self.stringInListForm = self.stack[self.index]


def main():
    sys.stdin = open("SimpleTextEditor_input.txt")

    word = TextEditor()

    n = int(input().strip())

    for _ in range(n):
        command = input().split()
        if command[0] == '1':
            word.appendString(command[1])
        elif command[0] == '2':
            word.deleteFromEnd(int(command[1]))
        elif command[0] == '3':
            word.printRequestedChar(int(command[1]))
        elif command[0] == '4':
            word.undoLastModification()

if __name__ == "__main__":
    main()

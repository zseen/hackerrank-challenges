import sys


class TextEditor:
    def __init__(self):
        self.stringInListForm = []
        self.operatingStack = []

    def appendString(self, ending):
        self.operatingStack.append(self.stringInListForm)
        self.stringInListForm = self.stringInListForm + list(ending)

    def deleteFromEnd(self, charsNumToSlice):
        self.operatingStack.append(self.stringInListForm)
        self.stringInListForm = self.stringInListForm[:-charsNumToSlice]

    def printRequestedChar(self, charToPrintIndex):
        print(self.stringInListForm[charToPrintIndex - 1])

    def undoLastModification(self):
        self.stringInListForm = self.operatingStack.pop()


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
        else:
            word.undoLastModification()

if __name__ == "__main__":
    main()

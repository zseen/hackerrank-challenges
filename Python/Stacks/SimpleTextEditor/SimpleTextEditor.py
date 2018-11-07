import sys


class TextEditor:
    def __init__(self):
        self.stringInListForm = []
        self.operatingStack = [self.stringInListForm]

    def appendString(self, ending):
        tempList = self.stringInListForm + list(ending)
        self.stringInListForm = tempList
        self.operatingStack.append(self.stringInListForm)

    def deleteFromEnd(self, charsNumToSlice):
        self.stringInListForm = self.stringInListForm[:-charsNumToSlice]
        self.operatingStack.append(self.stringInListForm)

    def printRequestedChar(self, charToPrintIndex):
        print(self.stringInListForm[charToPrintIndex - 1])

    def undoLastModification(self):
        self.operatingStack.pop()
        self.stringInListForm = self.operatingStack[-1]


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

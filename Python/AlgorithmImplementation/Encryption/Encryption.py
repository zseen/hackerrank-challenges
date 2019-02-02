import sys
from math import sqrt, ceil


def encryption(string):
    stringLength = len(string)
    columnsNum = ceil(sqrt(stringLength))
    encryptedString = []

    for i in range(0, columnsNum):
        encryptedString.append(string[i::columnsNum] + " ")

    return ''.join(encryptedString)


def main():
    sys.stdin = open("Encryption_input.txt")
    s = input()

    result = encryption(s)
    print(result)

if __name__ == '__main__':
    main()

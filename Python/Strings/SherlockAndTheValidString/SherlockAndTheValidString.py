import sys
from collections import Counter


def isValid(string):
    lettersCounter = Counter(string)
    valuesList = []

    for key, value in lettersCounter.items():
        valuesList.append(value)

    minValue = min(valuesList)
    maxValue = max(valuesList)

    if maxValue == minValue:
        return True
    elif maxValue - minValue == 1 and valuesList.count(maxValue) == 1:
        return True
    elif minValue == 1 and valuesList.count(minValue) == 1 and len(set(valuesList)) == 2:
        return True

    return False


def main():
    sys.stdin = open("SherlockAndTheValidString_input.txt")
    s = input()

    result = isValid(s)
    if result:
        res = "YES"
    else:
        res = "NO"
    print(res)

if __name__ == '__main__':
    main()

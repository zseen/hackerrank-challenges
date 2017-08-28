import sys


def countValleys(upAndDown):
    isDown = 0
    valley = 0
    upAndDownNumbers = []

    for item in upAndDown:
        if item == "U":
            upAndDownNumbers.append(1)
        elif item == "D":
            upAndDownNumbers.append(-1)

    for item in upAndDownNumbers:
        isDown += item
        if item == 1 and isDown == 0:
            valley += 1

    return valley


def main():
    sys.stdin = open('countingValley_input.txt')
    numberOfSteps = int(input().strip())
    upAndDown = list(input())
    numberOfValleys = countValleys(upAndDown)
    print(numberOfValleys)

if __name__ == "__main__":
    main()

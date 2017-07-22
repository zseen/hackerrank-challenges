import sys


def simpleArraySum(n, ar):
    arraySum = 0
    for elem in ar:
        arraySum += elem

    return arraySum


def main():
    sys.stdin = open('simplearraysum_input.txt') # redirect stdin to be from a file

    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    result = simpleArraySum(n, ar)
    print(result)

if __name__ == "__main__":
    main()

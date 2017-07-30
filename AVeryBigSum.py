import sys


def aVeryBigSum(listToSum):
    sumNumbers = 0
    for x in listToSum:
        sumNumbers += x

    return sumNumbers


def main():
    sys.stdin = open('AVeryBigSum_input.txt')
    listToSum = list(map(int, input().strip().split(' ')))
    HowManyNumbers = int(input().strip())
    result = aVeryBigSum(listToSum)
    print(result)

if __name__ == "__main__":
    main()
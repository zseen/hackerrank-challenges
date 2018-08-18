import sys


def aVeryBigSum(listToSum):
    sumNumbers = 0
    for x in listToSum:
        sumNumbers += x

    return sumNumbers


def main():
    sys.stdin = open('AVeryBigSum_input.txt')
    HowManyNumbers = int(input().strip())
    listToSum = list(map(int, input().strip().split(' ')))
    result = aVeryBigSum(listToSum)
    print(result)

if __name__ == "__main__":
    main()
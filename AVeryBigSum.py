import sys

def aVeryBigSum():
    listToSum = list(map(int, input().strip().split(' ')))
    sumNumbers = 0
    for x in listToSum:
        sumNumbers += x

    return sumNumbers


def main():
    sys.stdin = open('AVeryBigSum_input.txt')
    HowManyNumbers = int(input().strip())
    result = aVeryBigSum()
    print(result)

if __name__ == "__main__":
    main()
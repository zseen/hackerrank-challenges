import sys


def solve(a0, a1, a2, b0, b1, b2):
    APoints = [int(a0), int(a1), int(a2)]
    BPoints = [int(b0), int(b1), int(b2)]
    pointForA = 0
    pointForB = 0
    for x in range(len(APoints)):
            if APoints[x] > BPoints[x]:
                pointForA += 1
            elif APoints[x] < BPoints[x]:
                pointForB += 1
    return [pointForA, pointForB]


def main():
    sys.stdin = open('CompareTheTriplets_input.txt')
    a0, a1, a2 = input().strip().split(' ')
    b0, b1, b2 = input().strip().split(' ')
    result = solve(a0, a1, a2, b0, b1, b2)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()

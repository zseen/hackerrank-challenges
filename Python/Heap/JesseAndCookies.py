import sys
import heapq


def cookies(desiredSweetnessRate, cookiesList):
    operationsCounter = 0
    heapq.heapify(cookiesList)

    while len(cookiesList) > 1 and cookiesList[0] < desiredSweetnessRate:
            currentCookie = heapq.heappop(cookiesList)
            nextCookie = heapq.heappop(cookiesList)
            mergedCookie = (1 * currentCookie) + (2 * nextCookie)
            heapq.heappush(cookiesList, mergedCookie)
            operationsCounter += 1

    if cookiesList[0] >= desiredSweetnessRate:
        return operationsCounter

    return -1


if __name__ == '__main__':
    sys.stdin = open("JesseAndCookies_input.txt")

    nk = input().split()
    n = int(nk[0])

    desiredSweetnessRate = int(nk[1])
    cookiesList = list(map(int, input().rstrip().split()))

    result = cookies(desiredSweetnessRate, cookiesList)
    print(result)

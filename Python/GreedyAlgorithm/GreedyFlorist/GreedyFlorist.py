import sys


def getMinimumCost(friendsNum, flowersPricesList):
    flowersPricesList = sorted(flowersPricesList, reverse=True)
    purchasingFriendID = 0
    minimumSpentTotal = 0
    purchaseRound = 0

    for price in flowersPricesList:
        minimumSpentTotal += (purchaseRound + 1) * price

        if purchasingFriendID + 1 == friendsNum:
            purchasingFriendID = 0
            purchaseRound += 1
        else:
            purchasingFriendID += 1

    return minimumSpentTotal


def main():
    sys.stdin = open("GreedyFlorist_input.txt")
    nk = input().split()
    friendsNum = int(nk[1])
    flowersPricesList = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(friendsNum, flowersPricesList)
    print(minimumCost)

if __name__ == '__main__':
    main()

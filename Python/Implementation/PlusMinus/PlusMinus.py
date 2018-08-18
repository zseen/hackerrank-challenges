import sys


def PosNegZeroFractions(howManyNumbers,numbersList):
    positiveList = []
    negativeList = []
    zeroList = []
    for x in numbersList:
        if int(x) > 0:
            positiveList.append(x)
        elif int(x) < 0:
            negativeList.append(x)
        else:
            zeroList.append(x)


    negativeRatio = (len(negativeList)) / (howManyNumbers)
    positiveRatio = (len(positiveList)) / (howManyNumbers)
    zeroRatio = (len(zeroList)) / (howManyNumbers)

    return [positiveRatio, negativeRatio, zeroRatio]


def main():
    sys.stdin = open('PlusMinus_input.txt')
    howManyNumbers = int(input().strip())
    numbersList = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    fraction = PosNegZeroFractions(howManyNumbers, numbersList)
    for x in range(len(fraction)):
        print("{0:.6f}".format(round(fraction[x], 6)))


if __name__ == "__main__":
    main()



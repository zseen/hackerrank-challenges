import sys


def timeConversion(timePmAm):
    timeList = list(timePmAm)
    for item in range(0, len(timeList)):
        if "P" in timeList and "M" in timeList:
            deleteLastTwoChar(timeList)
            if timeList[0] == "0":
                del(timeList[0])
                timeList[0] = str(int(timeList[0]) + 12)
            elif timeList[0] == "1":
                if timeList[1] == "2":
                    pass
                else:
                    timeList[0] = str(int(timeList[0]) + 1)
                    timeList[1] = str(int(timeList[1]) + 2)
        elif "A" in timeList and "M" in timeList:
            deleteLastTwoChar(timeList)
            if timeList[0] == "1" and timeList[1] == "2":
                timeList[0] = "0"
                timeList[1] = "0"
    return "".join(timeList)


def deleteLastTwoChar(timeList):
    del (timeList[len(timeList) - 1])
    del (timeList[len(timeList) - 1])


def main():
    sys.stdin = open('timeconversion_input.txt')
    timePmAm = input().strip()
    result = timeConversion(timePmAm)
    print(result)


if __name__ == "__main__":
    main()



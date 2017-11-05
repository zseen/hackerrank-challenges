import sys


def reverseDay(daysList):
    reversedDays = []
    for day in daysList:
        reversedDays.append(int(str(day)[::-1]))
    return reversedDays


def isDayBeautiful(startDate, endDate, divisor):
    daysList = []
    for day in range(startDate, endDate + 1):
        daysList.append(day)
    revDays = reverseDay(daysList)


    beautiful = 0
    for revDay, day in zip(revDays, daysList):
        if abs(revDay-day) % divisor == 0:
            beautiful += 1

    return beautiful


def main():
    sys.stdin = open('beautifulDaysAtTheMovies_input.txt')
    startDate, endDate, divisor = input().strip().split(' ')
    datesAndDivisor = [int(startDate), int(endDate), int(divisor)]
    startDate = datesAndDivisor[0]
    endDate = datesAndDivisor[1]
    divisor = datesAndDivisor[2]
    numberOfBeautifulDays = isDayBeautiful(startDate, endDate, divisor)
    print(numberOfBeautifulDays)

if __name__ == "__main__":
    main()

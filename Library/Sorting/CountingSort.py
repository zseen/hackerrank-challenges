def sortListOfNumbers(listOfNumbers):
    sortedListOfNumbers = []

    biggestNum = max(listOfNumbers)
    smallestNum = min(listOfNumbers)

    counter = [0] * (biggestNum - smallestNum + 1)

    for item in listOfNumbers:
        counter[item - smallestNum] += 1

    for index in range(0, len(counter)):
        for amount in range(0, counter[index]):
            sortedListOfNumbers.append(index + smallestNum)
    return sortedListOfNumbers

myResults = []
with open('myResultsPrisoner.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        myResults.append(line)

        line = f.readline()




correctResults = []
with open('correctResultsPrisoner.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        correctResults.append(line)
        line = f.readline()



for i, x in zip(myResults, correctResults):
    if i != x:
        print(i,x)
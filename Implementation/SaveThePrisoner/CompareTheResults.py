myResults = []
with open('MyResultsPrisoner.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        myResults.append(line)
        line = f.readline()




correctResults = []
with open('CorrectResultsPrisoner.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        correctResults.append(line)
        line = f.readline()


c = 0
for i, x in zip(myResults, correctResults):
    if i != x:
        c += 1
print(c)
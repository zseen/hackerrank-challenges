mySolution = []
with open('resultCatsAndAMouse.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        mySolution.append(line)
        line = f.readline()
#print(mySolution)

goodSolution = []
with open('goodSolutionCats.txt') as g:
    line = g.readline()
    while line:
        line = line.strip()
        goodSolution.append(line)
        line = g.readline()
#print(goodSolution)

fail = []
for i in range(0,100):
    if goodSolution[i] != mySolution[i]:
        fail.append(i)
        fail.append(goodSolution[i])
        fail.append(mySolution[i])
print(fail)



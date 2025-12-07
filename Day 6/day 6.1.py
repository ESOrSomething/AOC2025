input = open("input.txt", "r").read().splitlines()

betterProblemList = []

for strNum in range(0, len(input[0].split())):
    betterProblemList.append([])

for lineNum in range(0,len(input)):
    for strNum in range(0, len(input[lineNum].split())):
        betterProblemList[strNum].append(input[lineNum].split()[strNum])

total = 0

import math
for i in betterProblemList:
    strToEval = ""
    for num in i[:-2]:
        strToEval += num + i[-1]
    strToEval += i[-2]
    total += eval(strToEval)

print(total)
input = open("input.txt", "r").read().splitlines()

betterProblemList = []

for i in range(0, len(input) - 1):
    for charNum in range(0, len(input[i])):
        if input[i][charNum] == " ":
            if not all(input[x][charNum] == " " for x in range(0, len(input))):
                input[i] = input[i][:charNum] + "X" + input[i][charNum+1:]



for strNum in range(0, len(input[0].split())):
    betterProblemList.append([])

for lineNum in range(0,len(input)):
    for strNum in range(0, len(input[lineNum].split())):
        betterProblemList[strNum].append(input[lineNum].split()[strNum])

total = 0

for i in betterProblemList:
    sortedNums = sorted(i[:-1], key=lambda x: len(x),reverse=True)
    nums = i[:-1]
    newProblemList = []
    for j in range(1, len(sortedNums[0]) + 1):
        newProblemList.append("")
        for number in nums:
            if number[j-1] != "X":
                newProblemList[j-1] += number[j-1]
    strToEval = ""
    for num in newProblemList[:-1]:
        strToEval += num + i[-1]
    strToEval += newProblemList[-1]
    total += eval(strToEval)

print(total)
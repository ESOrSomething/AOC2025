input = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

import itertools

count = 0

for line in input:
    tempLine = line
    strLen = len(line)
    maxStr = ""
    while len(maxStr) != 12:
        maxNum = 0
        maxID = 0
        for i in range(0, len(tempLine) + len(maxStr) - 11):
            if int(tempLine[i]) > maxNum:
                maxID = i
                maxNum = int(tempLine[i])
        maxStr += str(maxNum)
        tempLine = tempLine[maxID+1:]
    count += int(maxStr)
print(count)
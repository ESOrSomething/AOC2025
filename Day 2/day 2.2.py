input = open("input.txt", "r").read().split(',')
count = 0

for r in input:
    startID, endID = r.split('-')
    for i in range(int(startID), int(endID) + 1):
        d = False
        tempStr = str(i)
        if len(str(i)) == 2:
            if str(i)[0] == str(i)[1]:
                count += i
        else:
            for x in range(1, len(str(i)) - 1):
                if str(i) == tempStr[x:] + tempStr[:x] and not d:
                    count += i
                    d = True

print(count)
    
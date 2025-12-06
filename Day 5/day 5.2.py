input = open("input.txt", "r").read().split("\n\n")
ranges = input[0].splitlines()
count = 0

import re
ranges = [[int(y) for y in re.findall("[0-9]+", x)] for x in ranges]

ranges.sort(key=lambda x:(x[0], x[1]))

newRangeList = []

for rID in range(0, len(ranges)):
    if rID == 0:
        newRangeList.append(ranges[rID])
    else:
        if ranges[rID][1] > newRangeList[len(newRangeList)-1][1]:
            if ranges[rID][0] <= ranges[rID-1][1]:
                newRangeList[len(newRangeList)-1][1] = ranges[rID][1]
            else:
                newRangeList.append(ranges[rID])
        else:
            continue

count = 0

for r in newRangeList:
    count += r[1] - r[0] + 1

print(count)
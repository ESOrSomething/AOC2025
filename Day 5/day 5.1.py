input = open("input.txt", "r").read().split("\n\n")
ranges = input[0].splitlines()
IDs = input[1].splitlines()
count = 0

import re
ranges = [re.findall("[0-9]+", x) for x in ranges]

for id in IDs:
    if any(int(id) in range(int(y[0]), int(y[1]) + 1) for y in ranges):
        count += 1

print(count)
input = open("input.txt", "r").read().splitlines()

grid = []
for i in range(0, len(input)):
    grid.append([])
    for j in range(0, len(input[i])):
        grid[i].append(input[i][j])

from functools import lru_cache

@lru_cache
def testCoords(startI, startJ):
    if startI == len(grid) - 1:
        return 1
    elif grid[startI+1][startJ] == "^":
        return testCoords(startI+1, startJ-1) + testCoords(startI+1, startJ+1)
    else:
        return testCoords(startI+1, startJ)

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == "S":
            print(testCoords(i, j))
input = open("input.txt", "r").read().splitlines()

grid = []
for i in range(0, len(input)):
    grid.append([])
    for j in range(0, len(input[i])):
        grid[i].append(input[i][j])

continueToRun = True

splits = []
splitCount = 0

while continueToRun == True:
    newGrid = []
    for i in range(0, len(grid)):
        newGrid.append([])
        for j in range(0, len(grid[i])):
            newGrid[i].append(grid[i][j])
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == "S":
                newGrid[i+1][j] = "|"
            elif grid[i][j] == "|":
                if i+1 in range(0, len(grid)):
                    if grid[i+1][j] == "^":
                        newGrid[i+1][j-1] = "|"
                        newGrid[i+1][j+1] = "|"
                        if (i, j) not in splits:
                            splits.append((i, j))
                            splitCount += 1
                    else:
                        newGrid[i+1][j] = "|"
                else:
                    continueToRun = False
    grid = newGrid

print(splitCount)
input = open("input.txt", "r").read().splitlines()
grid = []
count = 0

keepRunning = True

for i in range(0, len(input)):
    grid.append([])
    for j in range(0, len(input[0])):
        grid[i].append(input[i][j])

counts = []

while keepRunning:
    removedPaper = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == "@":
                neighbors = 0
                if i-1 in range(0, len(grid)):
                    if j-1 in range(0, len(grid[0])):
                        if grid[i-1][j-1] == "@":
                            neighbors += 1
                    if j in range(0, len(grid[0])):
                        if grid[i-1][j] == "@":
                            neighbors += 1
                    if j+1 in range(0, len(grid[0])):
                        if grid[i-1][j+1] == "@":
                            neighbors += 1
                if i in range(0, len(grid)):
                    if j-1 in range(0, len(grid[0])):
                        if grid[i][j-1] == "@":
                            neighbors += 1
                    if j+1 in range(0, len(grid[0])):
                        if grid[i][j+1] == "@":
                            neighbors += 1
                if i+1 in range(0, len(grid)):
                    if j-1 in range(0, len(grid[0])):
                        if grid[i+1][j-1] == "@":
                            neighbors += 1
                    if j in range(0, len(grid[0])):
                        if grid[i+1][j] == "@":
                            neighbors += 1
                    if j+1 in range(0, len(grid[0])):
                        if grid[i+1][j+1] == "@":
                            neighbors += 1
                if neighbors < 4:
                    count += 1
                    removedPaper.append((i, j))
    for roll in removedPaper:
        x, y = roll
        grid[x][y] = "."
    if count in counts:
        keepRunning = False
    else:
        counts.append(count)
print(count)
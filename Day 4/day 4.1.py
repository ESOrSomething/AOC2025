input = open("input.txt", "r").read().splitlines()
grid = []
count = 0

for i in range(0, len(input)):
    grid.append([])
    for j in range(0, len(input[0])):
        grid[i].append(input[i][j])

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
print(count)
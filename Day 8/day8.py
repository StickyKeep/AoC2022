import numpy as np

grid = [list(map(int, line)) for line in open("Day 8/input.txt", "r").read().split()]

grid = np.array(grid)

numberOfRows = len(grid)
lenghtOfRow = len(grid[0])

visibleTrees = 0

for row in range(len(grid)):
    for column in range(len(grid[row])):
        tree = grid[row][column]
        if (column == 0 or np.amax(grid[row, :column]) < tree 
        or column ==  numberOfRows - 1 or np.amax(grid[row, (column + 1):]) < tree 
        or row == 0 or np.amax(grid[:row, column]) < tree 
        or row == lenghtOfRow - 1 or np.amax(grid[(row + 1):, column]) < tree): 
            visibleTrees += 1
    
print(f"Part 1: {visibleTrees}")
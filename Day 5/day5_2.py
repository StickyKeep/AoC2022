# Day 5, part 2. Might revisit this one later and not hardcode the stackgrid.

# https://adventofcode.com/2022/day/5

# Grid copypasted from input:

#         [H]     [W] [B]            
#     [D] [B]     [L] [G] [N]        
# [P] [J] [T]     [M] [R] [D]        
# [V] [F] [V]     [F] [Z] [B]     [C]
# [Z] [V] [S]     [G] [H] [C] [Q] [R]
# [W] [W] [L] [J] [B] [V] [P] [B] [Z]
# [D] [S] [M] [S] [Z] [W] [J] [T] [G]
# [T] [L] [Z] [R] [C] [Q] [V] [P] [H]


grid = [    ["P", "V", "Z", "W", "D", "T"],
    ["D", "J", "F", "V", "W", "S", "L"],
    ["H", "B", "T", "V", "S", "L", "M", "Z"],
    ["J", "S", "R"],
    ["W", "L", "M", "F", "G", "B", "Z", "C"],
    ["B", "G", "R", "Z", "H", "V", "W", "Q"],
    ["N", "D", "B", "C", "P", "J", "V"],
    ["Q", "B", "T", "P"],
    ["C", "R", "Z", "G", "H"]
]

for i in grid:
    i.reverse()

with open("Day 5/input.txt", "r") as f:
   for lines in f:
       clusterFgrid = []
       lines = lines.strip().split(" ")
       liftCounter = int(lines[1])
       fromNumber = int(lines[3])
       toNumber = int(lines[5])
       fromNumber -= 1
       toNumber -= 1
       i = 0
       for i in range(liftCounter):
             pop = grid[fromNumber].pop()
             clusterFgrid.insert(0, pop)
       grid[toNumber] += clusterFgrid 

solution = []

for line in grid:
    print(line)
    solution.append(line[-1])

print(("".join(solution)))

# Your puzzle answer was QRQFHFWCL 


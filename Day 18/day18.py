# Advent of Code 2022, Day 18, Part 1
# https://adventofcode.com/2022/day/13

drop_set = set()
counter = 0

OFFSET = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

with open("Day 18/input.txt") as f:
    for lines in f:
        x, y, z = map(int,lines.strip().split(","))
        drop_set.add((x,y,z))   

for (x, y, z) in drop_set:
    for (dx, dy, dz) in OFFSET:
        check = (x+dx, y+dy, z+dz)
        if check not in drop_set:
            counter += 1

print(counter)
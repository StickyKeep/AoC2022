from collections import defaultdict

path = []
size = 0
SIZE = defaultdict(int)
#SIZE = {}

with open("Day 7/input.txt", "r") as f:
    lineList = [line.strip().split(" ") for line in f]

for element in lineList:
    if element[0] == "$":
        if element [1] == "cd":
            if element[2] != "..":
                path.append(element[2])
                size = 0
            else:
                path.pop() 
                size = 0
    elif element[0] == "dir":
        continue
    else:
        size = int(element[0])
        for i in range(0,len(path)):
                SIZE['/'.join(path[:i+1])] += size
addorz = 0
for value in SIZE.values(): 
    if value <= 100000:
        addorz += value

print(f"part 1: {addorz}")

disk_size = 70000000
need = 30000000
need_to_free = need - (disk_size - SIZE['/'])

part2 = min(s for s in SIZE.values() if s >= need_to_free)
print(f'Part 2: {part2}')
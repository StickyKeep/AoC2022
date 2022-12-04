# Day 4, part 2: https://adventofcode.com/2022/day/4#part2 

# Find all pairs that overlap at all 

number_of_pairs_that_overlap = 0

with open("Day 4/input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for pairs in lines:
        a, b = pairs.split(",")
        a = a.split("-")
        b = b.split("-")
        a = [*range(int(a[0]), int(a[1])+1)]
        b = [*range(int(b[0]), int(b[1])+1)]
        check =  any(item in a for item in b) or any(item in b for item in a) # Just change all() to any() from part 1 code
        if check:
            number_of_pairs_that_overlap += 1
print(f"Number of contained pairs: {number_of_pairs_that_overlap}")

# Your puzzle answer was 821.
# Day 4, part 1: https://adventofcode.com/2022/day/4 

# In how many assignment pairs does one range fully contain the other? 

number_of_pairs = 0

with open("Day 4/input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for pairs in lines:
        a, b = pairs.split(",")
        a = a.split("-")
        b = b.split("-")
        a = [*range(int(a[0]), int(a[1])+1)]
        b = [*range(int(b[0]), int(b[1])+1)]
        check =  all(item in a for item in b) or all(item in b for item in a)
        if check:
            number_of_pairs += 1
print(f"Number of contained pairs: {number_of_pairs}")

# Your puzzle answer was 511.

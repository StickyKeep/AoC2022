# Advent of Code 2022, Day 13, Part 1
# https://adventofcode.com/2022/day/13

# Part 2 still out of reach; will come back to it later

input = [i.split("\n") for i in open("Day 13/in.txt", "r").read().strip("").split("\n\n")]

listCheck = lambda x: isinstance(x, list) # nice trick I picked up from a walkthrough
intCheck = lambda x: isinstance(x, int)

def compare(a, b):
    """Recursive check to churn down the nested lists and compare the ints"""
    if intCheck(a) and intCheck(b):
        return 1 if a > b else -1 if a < b else 0
    if listCheck(a) and listCheck(b):
        for i in range(min(len(a), len(b))):
            still_a_list = compare(a[i], b[i])
            if still_a_list: 
                return still_a_list
    if intCheck(a) and listCheck(b):
        a = [a]
        return compare(a, b)
    if listCheck(a) and intCheck(b):
        b = [b]
        return compare(a, b)
    return len(a) - len(b)

answer = 0

for index, (a,b) in enumerate(input, 1):
    if compare(eval(a), eval(b)) < 0:
        answer += index

print(answer)
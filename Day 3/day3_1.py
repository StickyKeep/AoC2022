# Day 3, part 1: https://adventofcode.com/2022/day/3 

# Revisited solution after reading some more 

priorityScore = 0

def prioritySolver(letter):
    if "a" <= letter <= "z": 
        return (ord(letter) - 96)
    else:
        return (ord(letter) - 38)

with open("Day 3/input.txt", "r") as f:
    for lines in f:
        line = lines.strip()
        rucksack1, rucksack2 = line[:len(line)//2], line[len(line)//2:]
        for letter in rucksack1:
            if letter in rucksack2:
                priorityScore += prioritySolver(letter)
                break

print(priorityScore)


##### OLD ANSWER BELOW ######

# common_items = []
# priority_sum = 0

# with open("Day 3/input.txt", "r") as f:
#     for line in f:
#         half_length = len(line) // 2
#         first_half = line[:half_length]
#         second_half = line[half_length:]
#         for item in first_half:
#             if item in second_half:
#                 common_items.append(item)
#                 break

# # Lowercase item types a through z have priorities 1 through 26.
# # Uppercase item types A through Z have priorities 27 through 52.

# #for lowercase we can use ord(x)-96 to get correct priority number
# #for uppercase we can use ord(X)-38 to get correct priority number

# for prio in common_items:
#     if prio.isupper() == True:
#         #print(prio)
#         priority_sum += (ord(prio) - 38)
#     if prio.islower() == True:
#         priority_sum += (ord(prio) - 96)

# print(priority_sum)
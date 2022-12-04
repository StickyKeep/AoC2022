# Day 3, part 2: https://adventofcode.com/2022/day/3#part2 
# Revisited solution after looking at some others and learning stuffz 

priorityScore = 0
counter = 0

def prioritySolver(letter):
    if "a" <= letter <= "z": 
        return (ord(letter) - 96)
    else:
        return (ord(letter) - 38)

with open("Day 3/input.txt", "r") as f:
    listOfLines = [line.strip() for line in f]
    while counter < len(listOfLines):
      for letter in listOfLines[counter]:
        if letter in listOfLines[counter+1] and letter in listOfLines[counter+2]:
          priorityScore += prioritySolver(letter)
          break
      counter += 3     
        
print(priorityScore)


### OLD SOLUTION BELOW ###

# This is a giant mess, but it somehow works.

# import re
# counter = 0
# count = 0
# common_list = []
# priority_sum = 0
# commons = []
# pattern = r'[A-Za-z]'

# with open('Day 3/input.txt', 'r') as input_file:
  
#   while count <= 99:
#     lines = [input_file.readline().strip() for _ in range(3)]
#     common = set.intersection(*map(set,lines))
#     common_list.append(common)
#     count += 1
#   common_list = str(common_list)
#   for chars in common_list:
#     if re.search(pattern, chars):
#         commons.append(chars)

# for prio in commons:
#     if prio.isupper() == True:
#         priority_sum += (ord(prio) - 38)
#     if prio.islower() == True:
#         priority_sum += (ord(prio) - 96)

# print(priority_sum)
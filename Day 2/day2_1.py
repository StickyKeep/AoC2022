# AoC 2022, day 2, part 1: https://adventofcode.com/2022/day/2 

# Revised solution after looking at others and learning new things.  

points = {"X": 1, "Y": 2, "Z": 3}
outcomes = {("A", "X"): 3, ("A", "Y"): 6, ("A", "Z"): 0, ("B", "X"): 0, ("B", "Y"): 3, ("B", "Z"): 6, ("C", "X"): 6, ("C", "Y"): 0, ("C", "Z"): 3}
score = 0 
with open("Day 2/input.txt", "r") as f:
        for line in f:
                line.strip()
                otherElf, me = line.strip().split(" ")
                score += points[me]
                score += outcomes[(otherElf, me)]
        print(score)
                


###### OLD SOLUTION BELOW ######


# # A = X = 1 rock
# # B = Y = 2 paper
# # C = Z = 3 sciss

# X = 1 # rock
# Y = 2 # paper
# Z = 3 # sciss

# win = 6
# loss = 0
# draw = 3

# total = 0

# with open("Day 2/input.txt", "r") as f:
#     for line in f:
#         x, y = line.split()
#         if x == "A" and y == "Y":
#                 total += win + Y
#                 print("win")
#         if x == "A" and y == "Z":
#                 print("loss")
#                 total += Z
#         if x == "B" and y == "X":
#                 print("loss")
#                 total += X
#         if x == "B" and y == "Z":
#                 print("win")
#                 total += win + Z
#         if x == "C" and y == "X":
#                 print("win")
#                 total += win + X
#         if x == "C" and y == "Y":
#                 print("loss")
#                 total += Y
#         if x == "A" and y == "X":
#                 total += draw + X
#         if x == "B" and y == "Y":
#                 total += draw + Y
#         if x == "C" and y == "Z":
#                 total += draw + Z

# print(total)
        
        
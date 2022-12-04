# AoC 2022, day 2, part 2: https://adventofcode.com/2022/day/2#part2 

# Revised solution after looking at others and learning new things:  

# New set of rules. X, Y and Z now denounces if I should lose, draw or win rock/paper/scissors. Just need to modify the dicts from 2-1.


points = {"X": 0, "Y": 3, "Z": 6}
outcomes = {("A", "Z"): 2, ("A", "X"): 3, ("A", "Y"): 1, ("B", "Z"): 3, ("B", "X"): 1, ("B", "Y"): 2, ("C", "Z"): 1, ("C", "X"): 2, ("C", "Y"): 3}
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

# X = 1 # rock A
# Y = 2 # paper B 
# Z = 3 # sciss C

# win = 6
# loss = 0
# draw = 3

# total = 0

# with open("Day 2/input.txt", "r") as f:
#     for line in f:
#         x, y = line.split()
#         if y == "X": # need to lose
#             if x == "A":
#                 total += Z
#             if x == "B":
#                 total += X
#             if x == "C":
#                 total += Y

#         if y == "Y": # need to draw
#             if x == "A":
#                 total += draw + X
#             if x == "B":
#                 total += draw + Y
#             if x == "C":
#                 total += draw + Z

#         if y == "Z": # need to win 
#             if x == "A":
#                 total += win + Y
#             if x == "B":
#                 total += win + Z
#             if x == "C":
#                 total += win + X

# print(total)
        
        
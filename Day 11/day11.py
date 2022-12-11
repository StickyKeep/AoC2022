# Advent of Code 2020, Day 11, Part 1 and 2
# https://adventofcode.com/2022/day/11

# This code is a mess. Maybe I'll clean it up later. Maybe not. 

monkeys = []
data = []

_gg = open("Day 11/in.txt", "r").read().strip().split("\n\n") # Test input
#_gg = open("Day 11/input.txt", "r").read().strip().split("\n\n") Real input


for index, instructions in enumerate(_gg): 
    data.append(instructions.split("\n"))

for index, monkeyinfo in enumerate(data):
    info = []
    info.append(list(int(i) for i in monkeyinfo[1].split(": ")[1].split(", ")))
    info.append(monkeyinfo[2].split("= ")[-1]) # math operation to calculate worry level
    info.append(int(monkeyinfo[3].split(" ")[-1])) # % test int
    info.append(int(monkeyinfo[4].split(" ")[-1])) # ifTrue -> to monkey nr. 
    info.append(int(monkeyinfo[5].split(" ")[-1])) # ifFalse -> to monkey nr.
    monkeys.append(info)

throws = [0] * len(monkeys)

# Gotta find the least common multiple of all the 
# monkeys' factors for the huge numbers in part 2: 

LCM = 1

for i in range(len(monkeys)):
    LCM *= monkeys[i][2]

#for i in range(20): #range part 1
for i in range(10000): # range part 2
    for index, monkey in enumerate(monkeys): 
        for worry in monkeys[index][0]:
            oldWorry = worry
            newWorry = eval("lambda old: " + monkeys[index][1])
            newWorry = newWorry(oldWorry)
            #new //= 3 #part 1, no division by 3 in part 2
            newWorry = newWorry % LCM 
            if newWorry % monkeys[index][2] == 0:
                monkeys[monkeys[index][3]][0].append(newWorry)
            else:
                monkeys[monkeys[index][4]][0].append(newWorry)
            throws[index] += 1
            monkeys[index][0] = []

throws = sorted(throws)
print(f"Answ: {throws[-1]*throws[-2]}") # Print sum of the two highest monkey throw counts
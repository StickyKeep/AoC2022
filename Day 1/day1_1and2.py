# Day 1, part 1 and 2: https://adventofcode.com/2022/day/1

listOfCalories = []
temporarySum = 0 

with open("Day 1/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            temporarySum = 0            
        else: 
            temporarySum += int(line)
            listOfCalories.append(temporarySum)
            
    print(f"The elf carrying most calories has: {max(listOfCalories)}")
    print(f"The top three elves carry: {sum(sorted(listOfCalories)[-3:])}")
    
  
        
# Day 6, part 1 and 2: https://adventofcode.com/2022/day/6

def numberOfUniqueLetters(number):   
    with open("Day 6/input.txt", "r") as f:
        line = f.readline()
        for n in range(len(line)):
            letterSlice = line[n:(n+number)]
            if len(set(letterSlice)) == number:
                print(letterSlice)
                print(n+number)
                break

                
# Part 1:
numberOfUniqueLetters(4)

# Part 2:
numberOfUniqueLetters(14)

            
   
          
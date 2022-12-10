instructions =  []
INSTRUCT = []
x_value = 1

with open("Day 10/input.txt", "r") as f:
    for lines in f:
        instructions.append(lines.strip("\n"))    
    for opcode in instructions:
        if opcode == "noop":
            INSTRUCT.append(x_value)
        else:
            INSTRUCT.append(x_value)
            INSTRUCT.append(x_value)  
            x_value += int(opcode.strip("addx "))
    
    stepValuePair = list(enumerate(INSTRUCT, 1))[19::40]
    sum = sum([x*y for x, y in stepValuePair])
    print(f"Sum part 1: {sum}")
    print("\nPart 2:\n")
    x = list(range(len(INSTRUCT)))

for i in range(0, len(INSTRUCT), 40): 
    for j in range(40):
        if abs(INSTRUCT[(i+j)] - j) <=1:
            print("#", end="")            
        else:
            print(" ", end="") 
            if (j+1) % 40 == 0:
                print("")
        
# answer part 2: 

###  #  #  ##  ####  ##    ## ###  ###  
#  # # #  #  #    # #  #    # #  # #  # 
#  # ##   #  #   #  #  #    # ###  #  # 
###  # #  ####  #   ####    # #  # ###  
# #  # #  #  # #    #  # #  # #  # # #  
#  # #  # #  # #### #  #  ##  ###  #  # 
# just fed everything into GPTchat and god this code as output :) 


# open the input file
with open("Day 1/input.txt") as f:
    # read the lines from the input file
    lines = f.readlines()

# remove the newline characters from each line
lines = [line.strip() for line in lines]

# create an empty list to store the food items
food_items = []

# create a temporary list to store the food items carried by a single Elf
temp = []

# iterate over the lines in the input
for line in lines:
    # if the line is empty, it indicates the end of the food items carried by an Elf
    if line == "":
        # add the temporary list to the main list of food items
        food_items.append(temp)
        # reset the temporary list
        temp = []
    else:
        # convert the line to an integer and add it to the temporary list
        temp.append(int(line))

# add the last temporary list to the main list of food items
food_items.append(temp)

# calculate the total number of Calories carried by each Elf
total_calories = [sum(elf) for elf in food_items]

# find the index of the Elf carrying the most Calories
most_calories_index = total_calories.index(max(total_calories))

# print the total number of Calories carried by the Elf carrying the most Calories
print(f"The Elf carrying the most Calories is carrying a total of {total_calories[most_calories_index]} Calories.")

horizontal = 0
depth = 0
aim = 0 # Part 2

file = open("input.txt", "r")
lines = file.readlines()

for line in lines:
    command = line.split(" ")
    if command[0] == "forward":
        horizontal += int(command[1])
        depth += (aim * int(command[1])) # Part 2
    if command[0] == "down":
        #depth += int(command[1]) # Part 1
        aim += int(command[1]) # Part 2
    if command[0] == "up":
        #depth -= int(command[1]) # Part 1
        aim -= int(command[1]) # Part 2

    print(aim, horizontal, depth)

position = horizontal * depth
print("position is:",position)
# Puzzle 1
previousValue = 0
depthIncreases = 0

file = open("input.txt", "r")
lines = file.readlines()

lines = map(int, lines)
lines = list(lines)

for line in lines:
    if line > previousValue and previousValue != 0:
        depthIncreases += 1
    previousValue = line

print("depth increases:", depthIncreases)
print("last value:", previousValue)

# Puzzle 2
previousValue = 0
depthIncreases = 0

def slidingWindow(elements, windowSize):
    groupedElements = []
    for i in range(len(elements) - windowSize + 1):
        groupedElements.append(sum(elements[i:i+windowSize]))
    return groupedElements


groupedElements = slidingWindow(lines, 3)

for element in groupedElements:
    if element > previousValue and previousValue != 0:
        depthIncreases += 1
    previousValue = element

print("depth increases:", depthIncreases)
print("last value:", previousValue)

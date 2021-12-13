# -*- coding: utf-8 -*-

file = open("input_grace.txt", "r")

lines = []
line = file.readline()
while line:
    lines.append(line)
    line = file.readline()
file.close()


# Part 1
        
illegalChars = []
for line in lines:   
    openList = []
    closedList = []
    i=0
    for c in line:

        if c == ')':
            if openList[-1] == '(':
                openList = openList[:-1]
            else:
                illegalChars.append(line[i])
                break
            closedList.append(c)
        elif c == '(':
            openList.append(c)
        elif c == ']':
            if openList[-1] == '[':
                openList = openList[:-1]
            else:
                illegalChars.append(line[i])
                break
            closedList.append(c)
        elif c == '[':
            openList.append(c)
        elif c == '}':
            if openList[-1] == '{':
                openList = openList[:-1]
            else:
                illegalChars.append(line[i])
                break
            closedList.append(c)
        elif c == '{':
            openList.append(c)
        elif c == '>':
            if openList[-1] == '<':
                openList = openList[:-1]
            else:
                illegalChars.append(line[i])
                break
            closedList.append(c)
        elif c == '<':
            openList.append(c)
        else:
            pass
        i+=1

rbPoints = 3
sbPoints = 57
cbPoints = 1197
chPoints = 25137


i = 0
for c in illegalChars:
    if c == ')':
        illegalChars[i] = rbPoints
    elif c == ']':
        illegalChars[i] = sbPoints
    elif c == '}':
        illegalChars[i] = cbPoints
    elif c == '>':
        illegalChars[i] = chPoints
    else:
        illegalChars[i] = 0
    i+=1
    
score = sum(illegalChars)
print('Score: ' + str(score))
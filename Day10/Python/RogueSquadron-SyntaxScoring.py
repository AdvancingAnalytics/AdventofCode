# -*- coding: utf-8 -*-

file = open("input_grace.txt", "r")

lines = []
line = file.readline()
while line:
    lines.append(line)
    line = file.readline()
file.close()


# Part 1
illegalLines = []    
illegalChars = []
j = 0
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
                illegalLines.append(j)
                break
            closedList.append(c)
        elif c == '(':
            openList.append(c)
        elif c == ']':
            if openList[-1] == '[':
                openList = openList[:-1]
            else:
                illegalChars.append(line[i])
                illegalLines.append(j)
                break
            closedList.append(c)
        elif c == '[':
            openList.append(c)
        elif c == '}':
            if openList[-1] == '{':
                openList = openList[:-1]
            else:
                illegalChars.append(line[i])
                illegalLines.append(j)
                break
            closedList.append(c)
        elif c == '{':
            openList.append(c)
        elif c == '>':
            if openList[-1] == '<':
                openList = openList[:-1]
            else:
                illegalChars.append(line[i])
                illegalLines.append(j)
                break
            closedList.append(c)
        elif c == '<':
            openList.append(c)
        else:
            pass
        i+=1
    j+=1

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
print('Part 1 Score: ' + str(score))

# Part 2

linesPart2 = lines

illegalLinesRev = illegalLines[::-1]
for l in illegalLinesRev:
    del linesPart2[l]
    
    
j = 0
completionStrings = []
completionLists = []
for line in linesPart2:   
    i=0
    openList = ['0']
    for c in line:
        if c == ')':
            if openList[-1] == '(':
                openList = openList[:-1]
            else:
                pass
        elif c == '(':
            openList.append(c)
        elif c == ']':
            if openList[-1] == '[':
                openList = openList[:-1]
            else:
                pass
        elif c == '[':
            openList.append(c)
        elif c == '}':
            if openList[-1] == '{':
                openList = openList[:-1]
            else:
                pass
        elif c == '{':
            openList.append(c)
        elif c == '>':
            if openList[-1] == '<':
                openList = openList[:-1]
            else:
                pass
        elif c == '<':
            openList.append(c)
        else:
            pass
        i+=1
    openListTotal = openList[1:]
    completeList = []
    for elem in openListTotal:
        if elem == '(':
            completeList.append(')')
        elif elem == '[':
            completeList.append(']')
        elif elem == '{':
            completeList.append('}')
        else:
            completeList.append('>')
    completeString = ''.join(completeList)
    completionStrings.append(completeString[::-1])
    completionLists.append(completeList[::-1])
    j+=1

rbScore = 1
sbScore = 2
cbScore = 3
chScore = 4
scores = []
for lst in completionLists:
    score = 0
    for elem in lst:
        score = score*5
        if elem == ')':
            score += rbScore
        elif elem == ']':
            score += sbScore
        elif elem == '}':
            score += cbScore
        elif elem == '>':
            score += chScore
        else:
            pass
    scores.append(score)
    
sortedList = sorted(scores)
midIndex = int((len(sortedList)/2)-0.5)

finalScore = sortedList[midIndex]

print('Part 2 Score: ' + str(finalScore))

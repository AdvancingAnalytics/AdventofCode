# Advent of Code
# Day 4


# Part 1

#import packages
import numpy as np

#ingest file

file = open("input_grace.txt", "r")
lines = file.readlines()


#split our drawn numbers list

drawnNumbers = lines[0].split(',')
drawnNumbers = list(np.array(drawnNumbers).astype(int))

strippedLines = lines[2:]

#loop through boards to create a list of arrays (each array is a bingo board)

for i in range(0,len(strippedLines)):
    strippedLines[i] = strippedLines[i].replace(' ',',').replace(',,',',')
    if strippedLines[i][0] == ',':
        strippedLines[i] = strippedLines[i][1:]
    strippedLines[i] = strippedLines[i].split(',')
            
            
boards = []
for l in range(0, len(strippedLines)-5, 6):
    boards.append(np.array(strippedLines[l:l+5]).reshape(5,5))
    
#play bingo

#collect the array and row index for each hit against a drawn numbers
#also collect the order in which the hit was marked off

allPositions = {}
c = 1
d = 0
for x in drawnNumbers:
    positionsForX = {}
    arrayCount = 0
    for array in boards:
        rowCount = 0
        for row in array:
            pos = np.where(row.astype(int) == x)
            if len(pos[0]) != 0:
                positionsForX[d] = [c,arrayCount, rowCount, pos[0][0]]  
                d+=1
            rowCount +=1
        arrayCount += 1
        allPositions[x] = positionsForX
    c+=1

#create a "check" board to mark the order of the bingo hits

#start with zeros
checkBoard = []
for l in range(0, len(strippedLines)-5, 6):
    checkBoard.append(np.zeros((5,5)))
    
#fill in bingo hits  
for x in drawnNumbers:
    for y in allPositions[x]:
        boardNumber = allPositions[x][y][1]
        rowNumber = allPositions[x][y][2]
        indexNumber = allPositions[x][y][3]
        orderNumber = allPositions[x][y][0]
        checkBoard[boardNumber][rowNumber][indexNumber] = orderNumber


#sum each row in the check boards
scoresRows = {}
rowCount = 0
for array in checkBoard:
    for row in array:
        tot = sum(row.astype(int))
        scoresRows[rowCount] = tot
        rowCount+=1
scoresCols = {}
colCount = 0
for array in checkBoard:
    for row in array.transpose():
        tot = sum(row.astype(int))
        scoresCols[colCount] = tot
        colCount+=1
        
# get lowest row - this will show the row that was completed first - this is bingo

lowestRowIndex = min(scoresRows, key = scoresRows.get)
lowestColIndex= min(scoresCols, key = scoresCols.get)
#find which board this row belongs to

lowestArray1 = (lowestRowIndex+1)//5 
lowestArrayRow = (lowestRowIndex)%5
print("array: "+str(lowestArray1), "row: "+str(lowestArrayRow))

lowestArray2 = (lowestColIndex+1)//5 
lowestArrayCol = (lowestColIndex)%5
print("array: "+str(lowestArray2), "col: "+str(lowestArrayCol))

winningRow = boards[lowestArray1][lowestArrayRow].astype(int)
winningCol = boards[lowestArray2].transpose()[lowestArrayCol].astype(int)

# find undrawn numbers in that board

indexesRow = []
for elem in winningRow:
    indexesRow.append(drawnNumbers.index(elem))
    
indexesCol = []
for elem in winningCol:
    indexesCol.append(drawnNumbers.index(elem))
    
winningDrawRow = int(drawnNumbers[max(indexesRow)].astype(int))
winningIndexRow = drawnNumbers.index(winningDrawRow)
    
winningDrawCol = int(drawnNumbers[max(indexesCol)].astype(int))
winningIndexCol = drawnNumbers.index(winningDrawCol)

winningIndex = min(winningIndexRow,winningIndexCol)
winningDraw = drawnNumbers[winningIndex]

if winningIndex == winningIndexRow:
    lowestArray = lowestArray1
else:
    lowestArray = lowestArray2
    
#for all numbers that were drawn after than the winning draw number, mark as 0
checkBoard[lowestArray][checkBoard[lowestArray1]>winningIndex+1] = 0
    
#get the indexes of all the 0s, and add the scores together from the bingo board of these numbers
listArrays = np.where(checkBoard[lowestArray] == 0)
length = len(listArrays[0])
uncheckedNumbers = []
for i in range(0, length):
    uncheckedNumbers.append([listArrays[0][i],listArrays[1][i]])
 
uncheckedNumbersScore = 0
for i in range(0,length):    
    uncheckedNumbersScore = uncheckedNumbersScore + int(boards[lowestArray][uncheckedNumbers[i][0]][uncheckedNumbers[i][1]])
    
# final score 

finalScore1 = uncheckedNumbersScore * winningDraw
print(finalScore1)
    
# Part 2 - DOESNT WORK YET

    
#sum each row in the check boards
scoresRows = {}
rowCount = 0
for array in checkBoard:
    for row in array:
        tot = sum(row.astype(int))
        scoresRows[rowCount] = tot
        rowCount+=1
scoresCols = {}
colCount = 0
for array in checkBoard:
    for row in array.transpose():
        tot = sum(row.astype(int))
        scoresCols[colCount] = tot
        colCount+=1
        

lowestArraysRows = []
lowestArraysCols = []
rowDict = {}
colDict = {}
scoreRow = 1000000
scoreCol = 1000000
while len(scoresRows) > 0:
    lowestRowIndex = min(scoresRows, key = scoresRows.get)
    lowestColIndex = min(scoresCols, key = scoresCols.get)
    lowestArray1 = (lowestRowIndex+1)//5 
    lowestArray2 = (lowestColIndex+1)//5 
    lowestArrayRow = (lowestRowIndex)%5
    lowestArrayCol = (lowestColIndex)%5
    lowestArraysRows.append(lowestArray1)
    lowestArraysCols.append(lowestArray2)
    if lowestArrayRow not in rowDict.keys() or min(scoresRows.values()) < scoreRow:
        rowDict[lowestArray1]=lowestArrayRow
    else:
        pass
    if lowestArrayCol not in colDict.keys() or min(scoresCols.values()) < scoreCol:
        colDict[lowestArray2]=lowestArrayCol
    else:
        pass
    scoreRow = min(scoresRows.values())
    scoreCol = min(scoresCols.values())
    del scoresRows[lowestRowIndex]
    del scoresCols[lowestColIndex]
    
uniqueArraysRows = []
for n in lowestArraysRows:
    if n not in uniqueArraysRows:
        uniqueArraysRows.append(n)
uniqueArraysCols = []
for m in lowestArraysCols:
    if m not in uniqueArraysCols:
        uniqueArraysCols.append(m)


highestArrayRows = uniqueArraysRows[-2]
#highestArrayRow = rowDict[highestArrayRows]
highestArrayCols = uniqueArraysCols[-2]
#highestArrayCol = colDict[highestArrayRows]

maxNumberRow = {}
i=0
for row in checkBoard[highestArrayRows]:
    maxNumberRow[i] = max(row)
    i+=1
    
lowestIndexRow = min(maxNumberRow, key = maxNumberRow.get)
highestArrayRow = lowestIndexRow


maxNumberCol = {}
i=0
for row in checkBoard[highestArrayCols].transpose():
    maxNumberCol[i] = max(row)
    i+=1
    
lowestIndexCol = min(maxNumberCol, key = maxNumberCol.get)
highestArrayCol = lowestIndexCol

print("array: "+str(highestArrayRows), "row: "+str(highestArrayRow))
print("array: "+str(highestArrayCols), "col: "+str(highestArrayCol))

winningRow = boards[highestArrayRows][highestArrayRow].astype(int)
winningCol = boards[highestArrayCols].transpose()[highestArrayCol].astype(int)


winningIndexRow = maxNumberRow[lowestIndexRow]
winningIndexCol = maxNumberCol[lowestIndexCol]

winningIndex = int(max(winningIndexRow,winningIndexCol))
winningDraw = drawnNumbers[winningIndex-1]

if winningIndex == winningIndexRow:
    highestArray = highestArrayRows
else:
    highestArray = highestArrayCols


#for all numbers that were drawn after than the winning draw number, mark as 0
checkBoard[highestArray][checkBoard[highestArray]>winningIndex+1] = 0

#get the indexes of all the 0s, and add the scores together from the bingo board of these numbers
listArrays = np.where(checkBoard[highestArray] == 0)
length = len(listArrays[0])
uncheckedNumbers = []
for i in range(0, length):
    uncheckedNumbers.append([listArrays[0][i],listArrays[1][i]])
 
uncheckedNumbersScore = 0
for i in range(0,length):    
    uncheckedNumbersScore = uncheckedNumbersScore + int(boards[highestArrayRows][uncheckedNumbers[i][0]][uncheckedNumbers[i][1]])
    
# final score 

finalScore2 = uncheckedNumbersScore * winningDraw
print(finalScore2)
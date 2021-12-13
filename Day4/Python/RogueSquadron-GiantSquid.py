# Advent of Code
# Day 4


# Set up Bingo Game (Run before each part)

#import packages
import numpy as np

#ingest file

file = open("input.txt", "r")
lines = file.readlines()


#split our drawn numbers list

drawnNumbers = lines[0].split(',')
drawnNumbers = list(np.array(drawnNumbers).astype(int))

strippedLines = lines[2:]

#loop through boards to create a list of arrays (each array is a bingo board)

def createBingoBoards(strippedLines):

    for i in range(0,len(strippedLines)):
        strippedLines[i] = strippedLines[i].replace(' ',',').replace(',,',',')
        if strippedLines[i][0] == ',':
            strippedLines[i] = strippedLines[i][1:]
        strippedLines[i] = strippedLines[i].split(',')
                
                
    boards = []
    for l in range(0, len(strippedLines)-5, 6):
        boards.append(np.array(strippedLines[l:l+5]).reshape(5,5))
    
    return boards

#play bingo

#collect the array and row index for each hit against a drawn numbers
#also collect the order in which the hit was marked off

def playBingo(boards):
    allPositions = {}
    c = 1
    d = 0
    for x in drawnNumbers:
        positionsForX = {}
        arrayCount = 0
        for array in boards:y
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
        
    #fill in bingo hits  - this plays a full game of bingo ignoring any wins, right through till all numbers have been drawn
    #the checkboard shows the order in which the numbers were marked off 
    for x in drawnNumbers:
        for y in allPositions[x]:
            boardNumber = allPositions[x][y][1]
            rowNumber = allPositions[x][y][2]
            indexNumber = allPositions[x][y][3]
            orderNumber = allPositions[x][y][0]
            checkBoard[boardNumber][rowNumber][indexNumber] = orderNumber
            
    return allPositions, checkBoard

boards = createBingoBoards(strippedLines)

# Part 1 Score

allPositions, checkBoard = playBingo(boards)

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
checkBoard[lowestArray][checkBoard[lowestArray1]>winningIndex+1] = 999
    
#get the indexes of all the 0s, and add the scores together from the bingo board of these numbers
listArrays = np.where(checkBoard[lowestArray] == 999)
length = len(listArrays[0])
uncheckedNumbers = []
for i in range(0, length):
    uncheckedNumbers.append([listArrays[0][i],listArrays[1][i]])

lst = []
uncheckedNumbersScore = 0
for i in range(0,length):    
    lst.append(int(boards[lowestArray][uncheckedNumbers[i][0]][uncheckedNumbers[i][1]]))
    uncheckedNumbersScore = uncheckedNumbersScore + int(boards[lowestArray][uncheckedNumbers[i][0]][uncheckedNumbers[i][1]])
    
# final score 

finalScore1 = uncheckedNumbersScore * winningDraw
print("Part 1 score: "+str(finalScore1))
    


# Part 2

allPositions, checkBoard = playBingo(boards)


minRowDict = {}
arrayCount = 0
for array in checkBoard:
    maxRows = []
    for row in array:
        maxRows.append(max(row))
    minNum = min(maxRows)
    loc = [np.where(array==minNum)[0][0], np.where(array==minNum)[1][0]]
    minRowDict[arrayCount] = [minNum, loc]
    arrayCount+=1

minColDict = {}
arrayCount = 0
for array in checkBoard:
    maxCols = []
    for row in array.transpose():
        maxCols.append(max(row))
    minNum = min(maxCols)
    loc = [np.where(array==minNum)[0][0], np.where(array==minNum)[1][0]]
    minColDict[arrayCount] = [minNum, loc]
    arrayCount+=1
    
minDict = {}
for key,val in zip(minRowDict, minColDict):
    if minRowDict[key][0] < minColDict[key][0]:
        minDict[key] = [minRowDict[key][0], minRowDict[key][1]]
    else:
        minDict[key] = [minColDict[key][0], minColDict[key][1]]
        
minOverall  = []
for key, val in minDict.items():
    minOverall.append(minDict[key][0])

maxWin = max(minOverall)
maxWinIndex = max(minDict, key = minDict.get)

maxRowIndex = minDict[maxWinIndex][1][0]
maxColIndex = minDict[maxWinIndex][1][1]


print("array: "+str(maxWinIndex), "row: "+str(maxRowIndex),"col: "+str(maxColIndex))

        
#for all numbers that were drawn after than the winning draw number, mark as 0
checkBoard[maxWinIndex][checkBoard[maxWinIndex]>maxWin] = 999

#get the indexes of all the 0s, and add the scores together from the bingo board of these numbers
listArrays = np.where(checkBoard[maxWinIndex] == 999)
length = len(listArrays[0])
uncheckedNumbers = []
for i in range(0, length):
    uncheckedNumbers.append([listArrays[0][i],listArrays[1][i]])
 
uncheckedNumbersScore = 0
for i in range(0,length):    
    uncheckedNumbersScore = uncheckedNumbersScore + int(boards[maxWinIndex][uncheckedNumbers[i][0]][uncheckedNumbers[i][1]])
    
# final score 

winningDraw = int(boards[maxWinIndex][maxRowIndex][maxColIndex])

finalScore2 = uncheckedNumbersScore * winningDraw
print("Part 2 score: "+str(finalScore2))
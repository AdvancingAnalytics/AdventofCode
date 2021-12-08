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

#calculate scores

#sum each row in the check boards
scores = {}
rowCount = 0
for array in checkBoard:
    for row in array:
        tot = sum(row.astype(int))
        scores[rowCount] = tot
        rowCount+=1
        
# get lowest row - this will show the row that was completed first - this is bingo

lowestRowIndex = min(scores, key = scores.get)

#find which board this row belongs to

lowestArray = (lowestRowIndex+1)//5 
lowestArrayRow = (lowestRowIndex)%5
print("array: "+str(lowestArray), "row: "+str(lowestArrayRow))

winningRow = boards[lowestArray][lowestArrayRow].astype(int)

# find undrawn numbers in that board

indexes = []
for elem in winningRow:
    indexes.append(drawnNumbers.index(elem))
    
winningDraw = int(drawnNumbers[max(indexes)].astype(int))
winningIndex = drawnNumbers.index(winningDraw)

#for all numbers that were drawn after than the winning draw number, mark as 0
checkBoard[lowestArray][checkBoard[lowestArray]>winningIndex+1] = 0
    
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

finalScore = uncheckedNumbersScore * winningDraw
print(finalScore)
    
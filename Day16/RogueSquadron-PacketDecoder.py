# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:49:27 2021

@author: GraceO'Halloran
"""
import textwrap

file = open("input_grace.txt")

lines = file.readlines()
line = lines[0]


convDictA = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100"
            , "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001"
            , "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110"
            , "F": "1111"}


convDictB = {"0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4"
            , "0101": "5", "0110": "6", "0111": "7", "1000": "8", "1001": "9"
            , "1010": "A", "1011": "B", "1100": "C", "1101": "D", "1110": "E"
            , "1111": "F"}

binaryLine = []
for l in line:
    newL = convDictA[l]
    binaryLine.append(newL)
    
binaryString = "".join(binaryLine)


"""
Define functions
"""

def getVersion(string):
    binaryVersion = "0" + string[0:3]
    decVersion = int(convDictB[binaryVersion])
    
    return decVersion

def getTypeID(string):
    binaryTypeID = "0" + string[3:6]
    decTypeID = int(convDictB[binaryTypeID])
    
    if decTypeID == 4:
        packetType = "L"
    else:
        packetType = "O"   
        
    return decTypeID, packetType

def getLengthTypeID(string):
    binaryLengthTypeID = string[6]
    
    if binaryLengthTypeID == "0":
        lengthType = "T"
    elif binaryLengthTypeID == "1":
        lengthType = "N"
    else:
        raise Exception("Length Type ID was neither 1 nor 0")
    
    return binaryLengthTypeID, lengthType

def readLiteralBits(string):
    remainingBits = string[6]
    
    bitList = textwrap.wrap(remainingBits, 5)
    
    i=0
    for bit in bitList:
        if bit[0] == "1":
            i+=1 
        elif bit[0] == "0":
            i+=1
            break
        else:
            pass
   
    packetBitList = bitList[:i]
    
    newList = []
    for bit in packetBitList:
        newBit = bit[1:]
        newList.append(newBit)
        
    bitString = "".join(newList)
    
    
    return bitString, packetBitList

def outputBits(string, packetBitList):
    decString = int(string,2)
    
    endOfPacket = 6 + len("".join(packetBitList))
    nextPacket = binaryString[endOfPacket:]
    
    return decString, nextPacket

"""
Start loop
"""

versions = []
totalLength = 0
while len(binaryString) > 0:
    version = getVersion(binaryString)
    versions.append(version)
    print(version)
    typeID, packetType = getTypeID(binaryString)
    print(typeID)
    if typeID == 4:
        packetType = "L"
        
        bitString, packetBitList = readLiteralBits(binaryString)
        decString, nextPacket = outputBits(bitString, packetBitList)
        binaryString = nextPacket
        
    else:
        packetType = "O"
        
        binaryLengthTypeID = binaryString[6]
        
        if binaryLengthTypeID == "0":
            lengthType = "T"
        elif binaryLengthTypeID == "1":
            lengthType = "N"
        else:
            raise Exception("Length Type ID was neither 1 nor 0")
            
        if lengthType == "T":
            totalLengthBits = binaryString[7:22]
            totalLength= int(totalLengthBits, 2)
            endIndex = 22 + totalLength
            remainingBits = binaryString[endIndex:]
            nextPacket = binaryString[22:-len(remainingBits)]
            binaryString = nextPacket
        else:
            numberPacketsBits = binaryString[7:18]
            numberPackets = int(numberPacketsBits, 2)
            endIndex = 18 + numberPackets
            remainingBits = binaryString[endIndex:]
            nextPacket = binaryString[28:-len(remainingBits)]
            binaryString = nextPacket
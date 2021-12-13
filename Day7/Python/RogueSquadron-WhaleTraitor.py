
from os import read
import statistics
from math import floor


file = open("input_grace.txt", "r")
line = file.readline().split(",")

line = list(map(int, line))

median = round(statistics.median(line))

fuelCost = 0

for i in line:
    fuelCost += abs(i - median)

print(fuelCost)

newFuelCost = 0
<<<<<<< HEAD
mean = round(statistics.mean(line))-1
=======
mean = floor(statistics.mean(line))-1
>>>>>>> 8a35e4613744663a5c8ff7c98c498c5a5f821074

for i in line:
    distance = abs(i - mean)
    gaussianNumber = (distance / 2) * (1 + distance)
    newFuelCost += gaussianNumber

print(newFuelCost)
print(mean)
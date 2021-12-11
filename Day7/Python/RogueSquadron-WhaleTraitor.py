
from os import read
import statistics


file = open("input.txt", "r")
line = file.readline().split(",")

line = list(map(int, line))

median = round(statistics.median(line))

fuelCost = 0

for i in line:
    fuelCost += abs(i - median)

print(fuelCost)

newFuelCost = 0
mean = round(statistics.mean(line))

for i in line:
    distance = abs(i - mean)
    gaussianNumber = (distance / 2) * (1 + distance)
    newFuelCost += gaussianNumber

print(newFuelCost)
print(mean)
import pandas as pd

file = open("input.txt", "r")
lines = file.readlines()

# Convert lines into Matrix
diagnostic_results = []
for line in lines:
    line = line.rstrip()
    diagnostic = [bit for bit in line]
    diagnostic_results.append(diagnostic)

#Convert Matrix into DataFrame
df = pd.DataFrame(diagnostic_results)

gamma = ""
epsilon = ""

for col in df:
    commonDenominator = pd.DataFrame(data=df[col].value_counts())
    
    gamma += commonDenominator.index[0]
    epsilon += commonDenominator.index[1]

print(gamma, epsilon)
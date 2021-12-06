
inputData = open('input.txt', 'r')
lines = inputData.readlines()

diagnostics = []
for line in lines:
    line = line.strip()
    diagnostics.append(line)

bitLen = len(diagnostics[0])

gammaRateBin = []
epsilonRateBin = []
bits = {}


for i in range(bitLen):
    for d in diagnostics:
        if not i in bits.keys():
            bits[i] = {}
        if not d[i] in bits[i].keys():
            bits[i][d[i]] = 0
        bits[i][d[i]] += 1

    gamma = 0 if bits[i]['0'] > bits[i]['1'] else 1
    epsilon = 0 if bits[i]['0'] < bits[i]['1'] else 1

    gammaRateBin.append(gamma)
    epsilonRateBin.append(epsilon)

gammaRateDec = int(''.join(map(str, gammaRateBin)), 2)
epsilonRateDec = int(''.join(map(str, epsilonRateBin)), 2)

powerRate = gammaRateDec * epsilonRateDec

print('Gamma rate bin: ', gammaRateBin)
print('Gamma rate dec: ', gammaRateDec)
print('Epsilon rate bin: ', epsilonRateBin)
print('Epsilon rate dec: ', epsilonRateDec)

print('Power rate: ', powerRate)

# assignment 4
import numpy as np
import re

# input uitlezen
lines = []
winners = []
values = []
numLines = []
with open('input.txt') as inputfile:
    inputstring = inputfile.read()
    input = inputstring.splitlines()
    for line in input:
        lines.append(re.split(':|\|',line)[1:])
    for i in range(0, len(lines)):                          # splitten in winnende getallen en eigen getallen, en die tuples mooi in een lijstje opslaan voor zometeen
        winners.clear()
        values.clear()
        for m in re.finditer('\d+', lines[i][0]):
            winners.append(m.group())
        for m in re.finditer('\d+', lines[i][1]):
            values.append(m.group())
        numLines.append((winners.copy(), values.copy()))

total = 0
totalCards = 0
cardInstances = np.ones(len(numLines), int)
for i in range(0,len(numLines)):
    value = 0
    wins = 0
    for j in range(0, len(numLines[i][1])):
        if numLines[i][1][j] in numLines[i][0]:             # als je getal tussen de winnende getallen staat heb je succes!
            if value == 0:
                value = 1
            else:
                value = value * 2
            wins += 1
    for j in range(i+1, min(i+wins+1, len(numLines))):      # even dat grimmige aantal kaartjes optellen
        cardInstances[j] += cardInstances[i]
    total += value
    totalCards += cardInstances[i]

# printen
# print(input)
# print(lines)
# print(numLines)
print(total)
print(totalCards)
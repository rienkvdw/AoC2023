# assignment 2
import numpy as np
import re

# input uitlezen
lines = []
with open('input.txt') as inputfile:
    inputstring = inputfile.read()
    input = inputstring.splitlines()
    for line in input:
        lines.append("." + line + ".")
width = len(lines[0])
edge = "." * width
lines.insert(0, edge)
lines.append(edge)

total = 0
stars = {}                                                      # als je naming ziet, zie je dat overeen komt. Het is inderdaad wederom geïnspireerd door de makker mjutn. Wel ben ik line voor line erdoorheen gegaan om te begrijpen wat er gebeurt.
gearTotal = 0
for i in range(1, len(lines)-1):
    num0 = 0
    num1 = 1
    for m in re.finditer('\d+', lines[i]):                      # de komende lines zijn compleet gejat van mjutn, want mijn vorige oplossing was kut en lelijk
        start,end = m.span()
        number = m.group()
        for j in range(i-1, i+2):
            for k in range(start-1, end+1):
                if not (lines[j][k] == "." or lines[j][k].isdigit()):   # dit minder mooie stukje is ook selfmade
                    total += int(number)                        # laatste gekopieerde line, want een printstatement kon ik wel lmfao
                
                if lines[j][k] == "*":                          # dat was een leugen van 3a Rienk, van hier tot de print statements is ook weer heerlijk geïnspireerd.
                    if (j,k) not in stars:
                        stars[(j,k)] = [int(number)]
                    else:
                        stars[(j,k)].append(int(number))

for key in stars:                                               
    if len(stars[key]) == 2:
        gearTotal += stars[key][0]*stars[key][1]

# printen
print(total)
print(gearTotal)
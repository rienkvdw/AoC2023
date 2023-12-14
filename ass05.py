# assignment 5
import numpy as np
import re

# input uitlezen
lines = []
maps = []
with open('input.txt') as inputfile:
    inputstring = inputfile.read()
    input = re.split(':', inputstring)
    for line in input:
        lines.append(line.splitlines())
    for i in range(0, len(lines)):
        for j in reversed(range(0, len(lines[i]))):
            if re.search('\d+', lines[i][j]) == None:
                lines[i].pop(j)
    lines.pop(0)
    seeds = []
    for m in re.finditer('\d+', lines[0][0]):
            seeds.append(int(m.group()))
    for i in range(1, len(lines)):
        mapje = {}
        for line in lines[i]:
            values = []
            for m in re.finditer('\d+',line):
                values.append(int(m.group()))
            mapje[values[1], values[1]+values[2]] = values[0] - values[1]
        maps.append(mapje)

lowLoc = 2147483647
lowLocInit = 0
for seedIndex in range(0, int(len(seeds)/2)):
    initSeed = seeds[seedIndex*2]
    print(initSeed)
    for seedje in range(seeds[seedIndex*2], seeds[seedIndex*2]+seeds[seedIndex*2+1]):
        seed = seedje
        for mapje in maps:
            for key in mapje:
                if seed in range(key[0],key[1]):
                    seed = seed + mapje[key]
                    break
        if seed < lowLoc:
            lowLoc = seed
            lowLocInit = initSeed

# printen
# print(lines)
# print(seeds)
# print(maps)
print(lowLoc)
print(lowLocInit)
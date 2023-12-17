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

# print(maps)
# mapComp = maps[0].copy()
# for mapje in maps[1:len(maps)]:
#     mapCompAdd = {}
#     for keyI in mapComp:
#         for keyJ in mapje:
#             lower = max(keyI[0]+mapComp[keyI],keyJ[0])
#             upper = min(keyI[1]+mapComp[keyI],keyJ[1])
#             print("KeyI: " + str(keyI) +  ", KeyJ: " + str(keyJ) + ", upper: " + str(upper) + ", lower: " + str(lower)) 
#             if upper > lower:
#                 mapCompAdd[lower-mapComp[keyI],upper-mapComp[keyI]] = mapComp[keyI] + mapje[keyJ]
#                 print("Added " + str((lower-mapComp[keyI],upper-mapComp[keyI])) + " with " + str(mapComp[keyI] + mapje[keyJ]))

#                 if keyI[0]+mapComp[keyI] > keyJ[0]:
#                     mapCompAdd[min(keyI[0]+mapComp[keyI],keyJ[0])-mapComp[keyI],lower-mapComp[keyI]] = mapje[keyJ]
#                     print("Added " + str((min(keyI[0]+mapComp[keyI],keyJ[0])-mapComp[keyI],lower-mapComp[keyI])) + " with " + str(mapje[keyJ]))
#                 else:
#                     mapCompAdd[min(keyI[0]+mapComp[keyI],keyJ[0])-mapComp[keyI],lower-mapComp[keyI]] = mapComp[keyI]
#                     print("Added " + str((min(keyI[0]+mapComp[keyI],keyJ[0])-mapComp[keyI],lower-mapComp[keyI])) + " with " + str(mapComp[keyI]))

#                 if keyI[1]+mapComp[keyI] > keyJ[1]:
#                     mapCompAdd[upper-mapComp[keyI],max(keyI[1]+mapComp[keyI],keyJ[1])-mapComp[keyI]] = mapComp[keyI]
#                     print("Added " + str((upper-mapComp[keyI],max(keyI[1]+mapComp[keyI],keyJ[1])-mapComp[keyI])) + " with " + str(mapComp[keyI]))

#                 else:
#                     mapCompAdd[upper-mapComp[keyI],max(keyI[1]+mapComp[keyI],keyJ[1])-mapComp[keyI]] = mapje[keyJ]
#                     print("Added " + str((upper-mapComp[keyI],max(keyI[1]+mapComp[keyI],keyJ[1])-mapComp[keyI])) + " with " + str(mapje[keyJ]))
#                 break
#             else:
#                 mapCompAdd[keyI] = mapComp[keyI]
#                 print("Added " + str(keyI) + " with " + str(mapComp[keyI]))
#                 mapCompAdd[keyJ] = mapje[keyJ]
#                 print("Added " + str(keyJ) + " with " + str(mapje[keyJ]))
#     print(mapComp)
#     mapComp.clear()
#     mapComp.update(mapCompAdd)
#     print(mapComp)
#     print()
#     break

# transforms = [list(range(0,100))]
# for mapje in maps:
#     huts = []
#     print(transforms[len(transforms)-1])
#     for i in range(0,len(transforms[len(transforms)-1])):
#         for key in mapje:
#             if transforms[len(transforms)-1][i] in range(key[0],key[1]):
#                 huts.append(transforms[len(transforms)-1][i]+mapje[key])
#                 break
        
#         if len(huts)-1 < i:
#             huts.append(transforms[len(transforms)-1][i])
#     transforms.append(huts)

# res = []
# for seedIndex in range (0, len(seeds),2):
#     initSeed = seeds[seedIndex]
#     while initSeed < seeds[seedIndex] + seeds[seedIndex+1]:
#         seed = initSeed
#         initSeed = 0
#         for mapje in maps:
#             for key in mapje:
#                 if seed in range(key[0],key[1]):
#                     seed = seed + mapje[key]
#                     break
#         res.append[seed]


res = []
for seedIndex in range(0, len(seeds), 2):
    seed_curr = seeds[seedIndex]
    while seed_curr < seeds[seedIndex] + seeds[seedIndex+1]:
        seed = seed_curr
        seed_curr = 0
        for mapje in maps:
            for key in mapje:
                if seed in range(key[0],key[1]):
                    if seed_curr == 0:
                        seed_curr = key[1]
                    seed = seed + mapje[key]
        print(seed)
        res.append(seed)

lowLoc = min(res)
for mapje in maps:
    for key in mapje:
        if lowLoc in range(key[0],key[1]):
            lowLoc = lowLoc + mapje[key]
            break

# printen
# print(lines)
# print(seeds)
print(res)
print(min(res))
print(lowLoc)

# for mapje in maps:
#     print(mapje)
# print(len(transforms))
# for i in range(0,len(transforms)):
#     print(transforms[i][:50])
# print()
# for i in range(0,len(transforms)):
#     print(transforms[i][50:])
# assignment 2
import numpy as np

# input uitlezen
with open('input.txt') as inputfile:
    inputstring = inputfile.read()
    input = inputstring.splitlines()

# (ID, r, g, b)

limits = (12,13,14)

inputs = []
for i in range(0,len(input)):
    x = input[i].split(":")
    inputs.append(x[1].split(";"))

succes = 0
status = np.ones(len(inputs))
powers = np.zeros(len(inputs))

for i in range(0, len(inputs)):
    mins = [0,0,0]
    for j in range(0, len(inputs[i])):
        for k in range (0, len(inputs[i][j])):
            if inputs[i][j][k].isdigit():
                if inputs[i][j][k+1].isdigit():     # grimmigheid omdat ik dom ben en multidigit getallen lastig vind
                    val = int(inputs[i][j][k])*10 + int(inputs[i][j][k+1])
                    match inputs[i][j][k+3]:
                        case "r":                   # check rood
                            if val > limits[0]:
                                status[i] = 0
                            if val > mins[0]:
                                mins[0] = val
                        case "g":                   # check groen
                            if val > limits[1]:
                                status[i] = 0
                            if val > mins[1]:
                                mins[1] = val
                        case "b":                   # check blauw
                            if val > limits[2]:
                                status[i] = 0
                            if val > mins[2]:
                                mins[2] = val

                else:                               # grimmigheid voor 1 digit
                    val = int(inputs[i][j][k])
                    match inputs[i][j][k+2]:
                        case "r":                   # check rood
                            if val > limits[0]:
                                status[i] = 0
                            if val > mins[0]:
                                mins[0] = val
                        case "g":                   # check groen
                            if val > limits[1]:
                                status[i] = 0
                            if val > mins[1]:
                                mins[1] = val
                        case "b":                   # check blauw
                            if val > limits[2]:
                                status[i] = 0
                            if val > mins[2]:
                                mins[2] = val
    if status[i] == 1:                              # even de makkers optellen
        succes += (i+1)
    powers[i] = mins[0]*mins[1]*mins[2]



## printen
# print(inputstring)
# print("inputlines: " + str(input))

# print(input)
# print(inputs)

print(succes)
print(sum(powers))
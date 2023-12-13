# assignment 2
import numpy as np

# functie zodat de main for loop een beetje leesbaar blijft
def checkAround(x, y):
    if x == 0:
        if y == 0:
            if not (input[x+1][y]       == "." or input[x+1][y].isdigit()):
                return True
            elif not (input[x][y+1]     == "." or input[x][y+1].isdigit()):
                return True
            elif not (input[x+1][y+1]   == "." or input[x+1][y+1].isdigit()):
                return True
            else:
                return False
        elif y == len(input[y])-1:
            if not (input[x][y-1]       == "." or input[x][y-1].isdigit()):
                return True
            elif not (input[x+1][y-1]   == "." or input[x+1][y-1].isdigit()):
                return True
            elif not (input[x+1][y]     == "." or input[x+1][y].isdigit()):
                return True
            else:
                return False
        else:
            print("kiekeboe, we zijn er " + str(x) + ", " + str(y))
            if not (input[x][y-1]       == "." or input[x][y-1].isdigit()):
                return True
            elif not (input[x+1][y-1]   == "." or input[x+1][y-1].isdigit()):
                return True
            elif not (input[x+1][y]     == "." or input[x+1][y].isdigit()):
                return True
            elif not (input[x][y+1]     == "." or input[x][y+1].isdigit()):
                return True
            elif not (input[x+1][y+1]   == "." or input[x+1][y+1].isdigit()):

                return True
            else:
                return False
    elif x == len(input)-1:
        if y == 0:
            if not (input[x-1][y]       == "." or input[x-1][y].isdigit()):
                return True
            elif not (input[x-1][y+1]   == "." or input[x-1][y+1].isdigit()):
                return True
            elif not (input[x][y+1]     == "." or input[x][y+1].isdigit()):
                return True
            else:
                return False
        elif y == len(input[y])-1:
            if not (input[x-1][y-1]     == "." or input[x-1][y-1].isdigit()):
                return True
            elif not (input[x][y-1]     == "." or input[x][y-1].isdigit()):
                return True
            elif not (input[x-1][y]     == "." or input[x-1][y].isdigit()):
                return True
            else:
                return False
        else:
            if not (input[x-1][y-1]     == "." or input[x-1][y-1].isdigit()):
                return True
            elif not (input[x][y-1]     == "." or input[x][y-1].isdigit()):
                return True
            elif not (input[x-1][y]     == "." or input[x-1][y].isdigit()):
                return True
            elif not (input[x-1][y+1]   == "." or input[x-1][y+1].isdigit()):
                return True
            elif not (input[x][y+1]     == "." or input[x][y+1].isdigit()):
                return True
            else:
                return False
    else:
        if y == 0:
            if not (input[x-1][y]       == "." or input[x-1][y].isdigit()):
                return True
            elif not (input[x+1][y]     == "." or input[x+1][y].isdigit()):
                return True
            elif not (input[x-1][y+1]   == "." or input[x-1][y+1].isdigit()):
                return True
            elif not (input[x][y+1]     == "." or input[x][y+1].isdigit()):
                return True
            elif not (input[x+1][y+1]   == "." or input[x+1][y+1].isdigit()):
                return True
            else:
                return False
        elif y == len(input[y])-1:
            if not (input[x-1][y-1]     == "." or input[x-1][y-1].isdigit()):
                return True
            elif not (input[x][y-1]     == "." or input[x][y-1].isdigit()):
                return True
            elif not (input[x+1][y-1]   == "." or input[x+1][y-1].isdigit()):
                return True
            elif not (input[x-1][y]     == "." or input[x-1][y].isdigit()):
                return True
            elif not (input[x+1][y]     == "." or input[x+1][y].isdigit()):
                return True
            else:
                return False
        else:
            if not (input[x-1][y-1]     == "." or input[x-1][y-1].isdigit()):
                return True
            elif not (input[x][y-1]     == "." or input[x][y-1].isdigit()):
                return True
            elif not (input[x+1][y-1]   == "." or input[x+1][y-1].isdigit()):
                return True
            elif not (input[x-1][y]     == "." or input[x-1][y].isdigit()):
                return True
            elif not (input[x+1][y]     == "." or input[x+1][y].isdigit()):
                return True
            elif not (input[x-1][y+1]   == "." or input[x-1][y+1].isdigit()):
                return True
            elif not (input[x][y+1]     == "." or input[x][y+1].isdigit()):
                return True
            elif not (input[x+1][y+1]   == "." or input[x+1][y+1].isdigit()):
                return True
            else:
                return False

# input uitlezen
with open('input.txt') as inputfile:
    inputstring = inputfile.read()
    input = inputstring.splitlines()

nums = []
inputDotted = input.copy()
for i in range(0, len(inputDotted)):        # ugly replace all non-digits with dots, for easier splitting
    for j in range(0, len(inputDotted[i])):
        if not inputDotted[i][j].isdigit():
            inputDotted[i] = inputDotted[i].replace(inputDotted[i][j],".")

for i in range(0, len(inputDotted)):        # make list of everything that isn't a dot
    nums.extend(inputDotted[i].split("."))

for i in reversed(range(0, len(nums))):     # remove any non-numbers
    if not nums[i].isdigit():
            nums.pop(i)

total = 0
numIndex = 0
endReached = False
# for i in range(0, len(input)):
#     for j in range(0, len(input[i])):
#         print("i = " + str(i) + ", j =  " + str(j) + ", numindex = " + str(numIndex) + ", nums[numindex] = " + str(nums[numIndex]) + ", len(nums[numIndex]) = " + str(len(nums[numIndex])))
#         if input[i][j:j+len(nums[numIndex])] == nums[numIndex]: # checken of het getal gelijk is aan het volgende verwachte number
#             print(str(input[i][j:j+len(nums[numIndex])]) + " matches " + str(nums[numIndex]))
#             for k in range(0,len(nums[numIndex])):
#                 print("checking: x = " + str(i) + ", y = " + str(j+k))
#                 if checkAround(i,j+k):                          # checken of er een charactertje omheen staat
#                     total += int(nums[numIndex])
#                     print("added " + str(nums[numIndex]) + " to total to make " + str(total))
#                     break
#             print("i = " + str(i) + ", j =  " + str(j) + ", numindex = " + str(numIndex) + ", nums[numindex] = " + str(nums[numIndex]) + ", len(nums[numIndex]) = " + str(len(nums[numIndex])))
#             jold = j
#             j = int((j + len(nums[numIndex])) % (len(input[i])-1))
#             i = i + int((jold + len(nums[numIndex])) / (len(input[i])-1))
#             numIndex += 1
#             if numIndex >= len(nums):                           # lelijke break statement
#                 endReached = True
#                 break
#     if endReached:
#         break

i = 0
j = 0
while i < len(input):
    while j < len(input[i]):
        if input[i][j:j+len(nums[numIndex])] == nums[numIndex]: # checken of het getal gelijk is aan het volgende verwachte number
            # print(str(input[i][j:j+len(nums[numIndex])]) + " matches " + str(nums[numIndex]))
            for k in range(0,len(nums[numIndex])):
                # print("checking: x = " + str(i) + ", y = " + str(j+k))
                if checkAround(i,j+k):                          # checken of er een charactertje omheen staat
                    total += int(nums[numIndex])
                    # print("added " + str(nums[numIndex]) + " to total to make " + str(total))
                    break
            iold = i
            jold = j
            inew = iold + int((jold + len(nums[numIndex])) / (len(input[iold])))
            jnew = int((jold + len(nums[numIndex])) % (len(input[iold])))
            i = int(inew)
            j = int(jnew)
            numIndex += 1
            if numIndex >= len(nums):                           # lelijke break statement
                endReached = True
                break
        else:
            iold = i
            jold = j
            inew = iold + int((jold+1)) / (len(input[iold]))
            jnew = int((jold + 1) % (len(input[iold])))
            i = int(inew)
            j = int(jnew)
    if endReached:
         break

# print("i = " + str(i) + ", j =  " + str(j) + ", numindex = " + str(numIndex) + ", nums[numindex] = " + str(nums[numIndex]) + ", len(nums[numIndex]) = " + str(len(nums[numIndex])))


# # printen
# print(inputstring)
# print("inputlines: " + str(input))
# print(nums)
print(total)                            # 532389 is te laag
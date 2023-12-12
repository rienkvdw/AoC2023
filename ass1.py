# assignment 1
import numpy as np

# input uitlezen
with open('input.txt') as inputfile:
    inputstring = inputfile.read()
    input = inputstring.splitlines()

# klein functietje voor leesbaarheid
def check_dig(inpString):
    val = 0
    if inpString[0].isdigit(): # als digit gewoon digit
        val = int(inpString[0])
    elif inpString.find("one") == 0: # anders de grimmige "case" statement
        val = 1
    elif inpString.find("two") == 0:
        val = 2
    elif inpString.find("three") == 0:
        val = 3
    elif inpString.find("four") == 0:
        val = 4
    elif inpString.find("five") == 0:
        val = 5
    elif inpString.find("six") == 0:
        val = 6
    elif inpString.find("seven") == 0:
        val = 7
    elif inpString.find("eight") == 0:
        val = 8
    elif inpString.find("nine") == 0:
        val = 9
    return(val)

# half onnodige init
num = np.zeros(len(input))
sum = 0

for i in range(0, len(input)):
    dig0 = 0
    dig1 = 0
    for j in range(0,len(input[i])):
        if (val := check_dig(input[i][j:])) != 0: # het stukje code dat daadwerkelijk bijna alles doet
            if dig1 == 0:
                dig1 = val
                dig0 = val
            else:
                dig0 = val
    num[i] = dig1*10+dig0
    sum += num[i]

# printen
print(inputstring)
print("inputlines: " + str(input))
print("numbers: " + str(num))
print("sum: "+ str(sum))
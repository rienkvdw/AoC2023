# assignment 6
import numpy as np
import re

# input uitlezen
with open('input.txt') as inputfile:
    inputstring = inputfile.read()
    input = inputstring.splitlines()
    lines = []
    for line in input:
        lines.append(re.sub("\s+", "", line))
    times = []
    for m in re.finditer('\d+', lines[0]):
        times.append(int(m.group()))
    distances = []
    for m in re.finditer('\d+', lines[1]):
        distances.append(int(m.group()))

nums = np.zeros(len(times), int)
for i in range(0, len(times)):
    for j in range(0, times[i]):
        speed = j
        distance = (times[i]-j)*j
        if distance > distances[i]:
            nums[i] += 1
num = np.prod(nums)

# printen
print(input)
print(times)
print(distances)
print(nums)
print(num)
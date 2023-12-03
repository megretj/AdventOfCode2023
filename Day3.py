import numpy as np
import re

def lineToArray(line,):
    # all points to -2
    # all signs to -1
    # turn into numpy array
    encodedLine = np.array([])
    for i in line:
        if i == '.':
            encodedLine
    return

def line_total(prev,curr,next):
    line_total = 0
    numbers_indices = re.finditer(pattern='\d+', string=curr)
    indices = [[number.start(),number.end()] for number in numbers_indices]
    #print(indices)
    for index in indices:
        count = False
        currentNumber = curr[index[0]:index[1]]
        #check sides
        if index[0] > 0 and curr[index[0]-1]!='.':
            count = True
            #print(currentNumber+" had previous")
        if index[1] < len(curr) and curr[index[1]] != '.':
            count = True
            #print(currentNumber+" had next "+curr[index[1]+1])
        # for i in [max(0,index[0]-1),min(index[1]+1,len(curr))]:
        #     if curr[i] != '.':
        #         print(currentNumber + ' current: '+ curr[i])
        #         count=True
        #check top and bottom
        for i in range(max(0,index[0]-1),min(index[1]+1,len(curr)-1)):
            if prev[i]!='.' or next[i]!='.':
                #print(currentNumber + 'previous: '+ prev[i]+' next: '+next[i])
                count = True
                break
        if count:
            line_total += int(curr[index[0]:index[1]])
        # else:
        #     print(curr[index[0]:index[1]])
    return line_total

def part1():
    total = 0
    with open('inputs/day3.txt') as file:
        # Turn file into array
        curr = file.readline().strip()
        prev = '.'*len(curr)
        next = file.readline().strip()
        total += line_total(prev,curr,next)
        for line in file:
            prev = curr
            curr = next
            next = line.strip()
            total += line_total(prev,curr,next)
        prev = curr
        curr = next
        next = '.'*len(curr)
        total += line_total(prev,curr,next)
        # find all numbers in the current line
        print(total)
        # for line in file:
        #     np.concatenate((schematic,lineToArray(line)),axis=0)
    return

def update_dict(key,currentNumber,dict):
    if key in dict:
        print(dict[key])
        dict[key].append(currentNumber)
        print(dict[key])
    else:
        
        dict[key] = [currentNumber]
        print(dict[key])
    return dict

def gimmeStars(prev,curr,next,dict,currIdx):
    numbers_indices = re.finditer(pattern='\d+', string=curr)
    indices = [[number.start(),number.end()] for number in numbers_indices]
    for index in indices:
        currentNumber = int(curr[index[0]:index[1]])
        #check sides
        if index[0] > 0 and curr[index[0]-1]=='*':
            update_dict(f"{currIdx}:{index[0]-1}",currentNumber,dict)
        if index[1] < len(curr) and curr[index[1]] == '*':
            update_dict(f"{currIdx}:{index[1]}",currentNumber,dict)
        #check top and bottom
        for i in range(max(0,index[0]-1),min(index[1]+1,len(curr)-1)):
            if prev[i]=='*':
                dict = update_dict(f"{currIdx-1}:{i}",currentNumber,dict)
            if next[i]=='*':
                dict = update_dict(f"{currIdx+1}:{i}",currentNumber,dict)
    return dict

def part2():
    total = 0
    starDict = {}
    with open('inputs/day3.txt') as file:
        currIdx = 0
        curr = file.readline().strip()
        prev = '.'*len(curr)
        next = file.readline().strip()
        starDict = gimmeStars(prev,curr,next,starDict, currIdx)
        for line in file:
            currIdx += 1
            prev = curr
            curr = next
            next = line.strip()
            starDict = gimmeStars(prev,curr,next,starDict, currIdx)
        prev = curr
        curr = next
        next = '.'*len(curr)
        starDict = gimmeStars(prev,curr,next, starDict, currIdx+1)
    print(starDict)
    for key,value in starDict.items():
        if len(value) == 2:
            total += value[0]*value[1]
    print(total)

part2()

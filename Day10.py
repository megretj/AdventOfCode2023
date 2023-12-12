import re
import math

symbols = ['|','-','.','7','F','J','L']

def findFirstCoordinate(map):
    for i, line in enumerate(map):
        for j, symbol in enumerate(line):
            if symbol == 'S':
                return i,j
    return 0,0

def findNext(map, row, col,comingFrom):
    if comingFrom != 'north' and row > 0 and map[row-1][col] in ['|','7','F','S'] and map[row][col] in ['|','L','J']:
        return row-1, col, 'south'
    if comingFrom != 'west' and col > 0 and map[row][col-1] in ['-','F','L','S'] and map[row][col] in ['-','J','7'] :
        return row, col-1, 'east'
    if comingFrom != 'south' and row < len(map)-1 and map[row+1][col] in ['|','L','J','S'] and map[row][col] in ['|','7','F']:
        return row+1, col, 'north'
    if comingFrom != 'east' and col < len(map[row])-1 and map[row][col+1] in ['-','J','7','S'] and map[row][col] in ['-','F','L']:
        return row, col+1, 'west'
    return -1, -1, ''

def inMap(map,row,col):
    if row >= 0 and col >= 0 and row < len(map) and col < len(map[row]):
        return True
    return False

def printDistanceMap(map):
    for line in map:
        lineStr = ''
        for symbol in line:
            if int(symbol) == -1:
                symbol = "_"
            elif int(symbol) == -2:
                symbol = "."
            elif int(symbol) == -3:
                symbol = "#"
            else:
                symbol = str(symbol)
            
            lineStr = lineStr + " " + symbol 
        print(lineStr)
    return 

def consised(map):
    out = ''
    for line in map:
        lineStr = ''
        for symbol in line:
            if int(symbol) == -1:
                symbol = "_"
            elif int(symbol) == -2:
                symbol = "."
            elif int(symbol) == -3:
                symbol = "#"
            else:
                symbol = "x"
            
            lineStr = lineStr + symbol 
        out += lineStr + '\n'
    return out

def neighbourIsExplored(row,col,distanceMap):
    for i in [row-1,row,row+1]:
        for j in [col-1,col,col+1]:
            if inMap(distanceMap,i,j) and [i,j] != [col,row] and distanceMap[i][j] < -1:
                distanceMap[row][col] = distanceMap[i][j]
                return distanceMap, True
    return distanceMap, False
# if coordinate == -1 then it is not expored yet
# if >=0 then it's on the loop
# if == -2 then it is outiside the loop
# if == -3 then it's inside the loop.
def checkInside(row,col,distanceMap,maxDistance):
    print("evaluating "+str(row)+ ' ' +str(col))
    distanceMap, isGood = neighbourIsExplored(row, col,distanceMap)
    if not isGood:
        horizontalRightCrossings = 0
        previous = -10
        for i,horizontalRight in enumerate(distanceMap[row][col:]):
            if horizontalRight >= 0 and i!=col and (previous<0 or not (horizontalRight == (previous+1)%maxDistance or horizontalRight == (previous-1)%maxDistance)):
                horizontalRightCrossings+=1
            if horizontalRight >= 0:
                previous = horizontalRight
        print(horizontalRightCrossings)
        if horizontalRightCrossings%2 == 0: #figure out the crossings thing
            distanceMap[row][col] = -2
            return distanceMap
        horizontalLeftCrossings = 0
        previous = distanceMap[row][col]
        for i,horizontalLeft in enumerate(distanceMap[row][0:col]):
            if horizontalLeft >= 0 and i!=col and (previous<0 or not (horizontalLeft == (previous+1)%maxDistance or horizontalLeft == (previous-1)%maxDistance)):
                horizontalLeftCrossings+=1
            if horizontalLeft >= 0:
                previous = horizontalLeft
        print(horizontalLeftCrossings)
        if horizontalLeftCrossings%2 == 0: #figure out the crossings thing
            distanceMap[row][col] = -2
            return distanceMap
        verticalTopCrossings = 0
        previous = -10
        for i in range(row):# check the verticals
            verticalTop = distanceMap[i][col]
            if verticalTop >= 0 and i!=row and (previous<0 or not (verticalTop == (previous+1)%maxDistance or verticalTop == (previous-1)%maxDistance)):
                verticalTopCrossings+=1
            previous = verticalTop
        if verticalTopCrossings%2 == 0:
            distanceMap[row][col] = -2
            return distanceMap
        verticalBotCrossings = 0
        previous = -10
        for i in range(row,len(distanceMap)):# check the verticals
            verticalBot = distanceMap[i][col]
            if verticalBot >= 0 and i!=row and (previous<0 or not (verticalBot == (previous+1)%maxDistance or verticalBot == (previous-1)%maxDistance)):
                verticalBotCrossings+=1
            previous = verticalBot
        if verticalBotCrossings%2 == 0:
            distanceMap[row][col] = -2
            return distanceMap
        else:
            distanceMap[row][col] = -3
    return distanceMap

def part1():
    with open('inputs/day10.txt') as file:
        map = [[symbol for symbol in re.findall('.',line)] for line in file]
    rowS, colS = findFirstCoordinate(map)
    distanceMap = [[-1 for symbol in line] for line in map]
    distanceMap[rowS][colS] = 0
    #print(map)
    #print(distanceMap)
    nSteps = 0
    comingFrom = 'start'
    firstStepsTried = 0
    firstSteps = []
    firstStepsDirection = []
    neighbours = [[rowS-1, colS],[rowS, colS-1],[rowS+1, colS],[rowS, colS+1]]
    neighboursDirection = ['south','west','north','east']
    neighboursPossibleSymbol = [['|','7','F'],['-','F','L'],['|','L','J'],['-','J','7']]
    for i, neighbour in enumerate(neighbours):
        if inMap(map, neighbour[0],neighbour[1]) and map[neighbour[0]][neighbour[1]] in neighboursPossibleSymbol[i]:
            firstSteps.append(neighbour)
            firstStepsDirection.append(neighboursDirection[i])
    row, col = firstSteps[0]
    comingFrom = firstStepsDirection[0]
    nSteps = 1
    while not map[row][col] == 'S':
        # print(row, col, map[row][col],comingFrom)
        distanceMap[row][col] = nSteps
        row, col, comingFrom = findNext(map, row, col, comingFrom)
        nSteps += 1
        if row == -1 and col == -1:
            row, col = firstSteps[firstStepsTried]
            comingFrom = neighboursDirection[firstStepsTried]
            # Reinitialize distanceMap
            distanceMap = [[-1 for symbol in line] for line in map]
            distanceMap[rowS][colS] = 0
            firstStepsTried += 1
            nSteps = 1
    print(row, col)
    printDistanceMap(distanceMap)
    print(math.ceil(nSteps/2))
    return

def part2():
    with open('inputs/examples/day10.txt') as file:
        map = [[symbol for symbol in re.findall('.',line)] for line in file]
    rowS, colS = findFirstCoordinate(map)
    distanceMap = [[-1 for symbol in line] for line in map]
    distanceMap[rowS][colS] = 0
    nSteps = 0
    comingFrom = 'start'
    firstStepsTried = 0
    firstSteps = []
    firstStepsDirection = []
    neighbours = [[rowS-1, colS],[rowS, colS-1],[rowS+1, colS],[rowS, colS+1]]
    neighboursDirection = ['south','west','north','east']
    neighboursPossibleSymbol = [['|','7','F'],['-','F','L'],['|','L','J'],['-','J','7']]
    for i, neighbour in enumerate(neighbours):
        if inMap(map, neighbour[0],neighbour[1]) and map[neighbour[0]][neighbour[1]] in neighboursPossibleSymbol[i]:
            firstSteps.append(neighbour)
            firstStepsDirection.append(neighboursDirection[i])
    row, col = firstSteps[0]
    comingFrom = firstStepsDirection[0]
    nSteps = 1
    while not map[row][col] == 'S':
        # print(row, col, map[row][col],comingFrom)
        distanceMap[row][col] = nSteps
        row, col, comingFrom = findNext(map, row, col, comingFrom)
        nSteps += 1
        if row == -1 and col == -1:
            row, col = firstSteps[firstStepsTried]
            comingFrom = neighboursDirection[firstStepsTried]
            # Reinitialize distanceMap
            distanceMap = [[-1 for symbol in line] for line in map]
            distanceMap[rowS][colS] = 0
            firstStepsTried += 1
            nSteps = 1
    print(row, col)
    printDistanceMap(distanceMap)
    print('nSteps')
    print(nSteps)
    print(math.ceil(nSteps/2))
    maxDistance = nSteps
    for i, row in enumerate(distanceMap):
        for j, point in enumerate(row):
            if point == -1:
                distanceMap = checkInside(i,j,distanceMap,maxDistance)
    printDistanceMap(distanceMap)
    numberOfHashtags = 0
    for line in distanceMap:
        for symbol in line:
            if symbol == -3:
                numberOfHashtags += 1
    print(nSteps)
    print(numberOfHashtags)
    """ with open('output.txt','a') as f:
        print(consised(distanceMap),file = f) """
    return

""" def part2():
    # Idea for part 2 is to have two array, one with the map
    with open('inputs/day10.txt') as file:
        map = [[symbol for symbol in re.findall('.',line)] for line in file]
    rowS, colS = findFirstCoordinate(map)
    print(map)
    # One with the distance to S, -1 otherwise.
    distanceMap = [[-1 for symbol in line] for line in map]
    # The one with distances to S, we can simply put ones everywhere where there is 
    # Then, for every point that is not on the loop, count the number of parts of the loop it traverses in each direction.
    # If that number is even then the point is outside.

    return """

part2()
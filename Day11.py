import re
import copy
def inputToList(path):
    with open(path) as file:
        listOfList = [[symbol for symbol in re.findall('.',line)] for line in file]
    return listOfList

def scaleImage(image):
    # First scale empty rows
    newImage = []
    emptyRow = ['.' for i in range(len(image[0]))]
    for i, row in enumerate(image):
        empty = True
        for pixel in row:
            if pixel != '.':
                empty = False
        newImage.append(row[:])
        if empty:
            for _ in range(1000000):
                newImage.append(emptyRow[:])
    # Then scale empty columns
    EmptyCols = []
    for col in range(len(image[0])):
        emptyCol = True
        for row in image:
            if row[col] != '.':
                emptyCol = False
        if emptyCol:
            EmptyCols.append(col)
    for colId, column in enumerate(EmptyCols):
        for row in newImage:
            for i in range(1000000):
                row.insert(colId*1000000+column+i,'.')
    return copy.deepcopy(newImage)

def printImage(image):
    outputString = ''
    for row in image:
        rowString = ''
        for pixel in row:
            rowString += pixel
        outputString += rowString + '\n'
    print(outputString)
    return

def part1():
    image = inputToList('inputs/day11.txt')
    printImage(image)
    scaledImage = scaleImage(image)
    #printImage(scaledImage)
    # Now list all the galxies
    galaxies = []
    for i, row in enumerate(scaledImage):
        for j, pixel in enumerate(row):
            if pixel == '#':
                galaxies.append([i,j])
    distances = 0
    for galaxyId, galaxy in enumerate(galaxies[:-1]):
        for otherGalaxy in galaxies[galaxyId+1:]:
            distances += abs(galaxy[0]-otherGalaxy[0]) + abs(galaxy[1]-otherGalaxy[1])
    print(distances)
    # For every pair of galaxy, 
    return

def scaleRow(image):
    EmptyRows = []
    for row in image:
        emptyRow = True
        for pixel in row:
            if pixel != '.':
                emptyRow = False
        if emptyRow:
            EmptyRows.append(1000000)
        else:
            EmptyRows.append(1)
    return EmptyRows

def scaleCol(image):
    EmptyCols = []
    for col in range(len(image[0])):
        emptyCol = True
        for row in image:
            if row[col] != '.':
                emptyCol = False
        if emptyCol:
            EmptyCols.append(1000000)
        else:
            EmptyCols.append(1)
    return EmptyCols

def part2():
    image = inputToList('inputs/day11.txt')
    distancesRow = scaleRow(image)
    distancesCol = scaleCol(image)
    # print(distancesRow)
    # print(distancesCol)
    galaxies = []
    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            if pixel == '#':
                galaxies.append([i,j])
    distances = 0
    for galaxyId, galaxy in enumerate(galaxies[:-1]):
        for otherGalaxy in galaxies[galaxyId+1:]:
            distances += sum(distancesRow[galaxy[0]:otherGalaxy[0]]) + sum(distancesCol[min(galaxy[1],otherGalaxy[1]):max(galaxy[1],otherGalaxy[1])])
            #print("From " + str(galaxy) + " to "+ str(otherGalaxy) + " distance " + str(sum(distancesRow[galaxy[0]:otherGalaxy[0]]) + sum(distancesCol[galaxy[1]:otherGalaxy[1]])))
    print(distances)
    return 
    
part2()

# For part 2 instead of creating a new array, store two arrays that give the distance between the rows and the columns
# ..#.
# ....
# #..#
# would yield:
# rowdistance = [0,1000000]
# coldistance = [0,1000000,1].
# then to take the distance, one just needs to take the difference in the indices from these lists.
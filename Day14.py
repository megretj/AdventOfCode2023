import re

def findFirst(column):
    # Returns the first index at which there is not a '.' and what type of rock it is
    for i,symbol in enumerate(column):
        if symbol == '#':
            return symbol,i
        if symbol == 'O':
            return symbol,i
    return '.',-1

def reorderColumn(column,topRock):
    # column is an array where we want to reorder the rocks
    rockType, rockIdx = findFirst(column[topRock+1:])
    if rockIdx == -1: # Only '.' left in column
        #print(column)
        return column
    elif rockType == 'O': # No rolling rock until a blocking rock just swap the indices.
        column[topRock+1+rockIdx] = '.'
        column[topRock+1] = 'O'
    return reorderColumn(column,topRock+1)

def part1():
    total = 0
    with open('inputs/day14.txt') as file:
        # Find a way to split the file on empty lines
        # Don't need it here though
        rows = [line.strip() for line in file]
        columns = [[row[i] for row in rows] for i in range(len(rows[0]))]
    for column in columns:
        #print(column)
        total += sum([i+1 if rockIndex == 'O' else 0 for i,rockIndex in enumerate(reversed(reorderColumn(column,-1)))])
    print(total)
    return

def goNorth(columns, reversed = False):
    for j, column in enumerate(columns):
        if reversed:
            reversedcolumn = [column[i] for i in range(len(column)-1,-1,-1)]
            reversedcolumn = reorderColumn(reversedcolumn,-1)
            columns[j] = [reversedcolumn[i] for i in range(len(reversedcolumn)-1,-1,-1)]
        else:
            column = reorderColumn(column,-1)
    return [[col[i] for col in columns] for i in range(len(columns[0]))], columns

def goWest(rows, reversed = False):
    for j,row in enumerate(rows):
        if reversed:
            reversedrow = [row[i] for i in range(len(row)-1,-1,-1)]
            reversedrow = reorderColumn(reversedrow,-1)
            rows[j] = [reversedrow[i] for i in range(len(reversedrow)-1,-1,-1)]
        else:
            row = reorderColumn(row,-1)
    return rows, [[row[i] for row in rows] for i in range(len(rows[0]))]

def printImage(image):
    outputString = ''
    for row in image:
        rowString = ''
        for pixel in row:
            rowString += pixel
        outputString += rowString + '\n'
    #print(outputString)
    return outputString

def stringify(image):
    imgstr=''
    for row in image:
        for pixel in row:
            imgstr+=pixel
    return imgstr

def part2():
    total = 0
    # as soon as we enter a stable state, we don't need to turn again.
    with open('inputs/examples/day14.txt') as file:
        # Find a way to split the file on empty lines
        # Don't need it here though
        rows = [line.strip() for line in file]
        columns = [[row[i] for row in rows] for i in range(len(rows[0]))]
    a = 10
    adone = 0
    subtotal = 0
    for column in columns:
        subtotal += sum([i+1 if rockIndex == 'O' else 0 for i,rockIndex in enumerate(reversed(reorderColumn(column,-1)))])
    ogImage = ""
    memory={}
    # Now I'm only checking for loops from the first iteration, I need to check for loops at any point 
    # since the loop can appear at any point. Use dictionnaries and string views of the positions.
    # Two dictionnaries: string to index, index to subtotal
    # Once we find a loop, find the number of steps left to 1000000000 from there, modulo cycle length. And revert back 
    while (stringify(rows) != ogImage or adone == 1) and a > 0:
        rows, columns = goNorth(columns)
        rows, columns = goWest(rows)
        rows, columns = goNorth(columns,True)
        rows, columns = goWest(rows,True)
        subtotal = 0
        for column in columns:
            subtotal += sum([i+1 if rockIndex == 'O' else 0 for i,rockIndex in enumerate(reversed(column))])
        #print(subtotal)
        memory[adone] = subtotal
        a -= 1
        adone +=1
        if adone == 1:
            ogImage = stringify(rows)
        print(stringify(rows))
        print(ogImage)
        #print(memory)

    print(adone)
    indexOnCycle = 1000000000%(adone+1)
    print(memory[indexOnCycle])
    """ while ogRows != rows and a > 0:
        a -= 1
        adone +=1
        ogRows = rows[:]
        rows, columns = goNorth(columns)
        rows, columns = goWest(rows)
        rows, columns = goNorth(columns,True)
        rows, columns = goWest(rows,True)
    for column in columns:
        #print(column)
        total += sum([i+1 if rockIndex == 'O' else 0 for i,rockIndex in enumerate(reversed(column))])
    print(str(total)+ "with "+ str(a) + " iterations left.") """
    return 
part2()
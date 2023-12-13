import re 


def pairs(pattern):
    pairs = []
    for i,j in enumerate(pattern[:-1]):
        if pattern[i+1] == j:
            pairs.append(i)
    return pairs

def isPalindrome(array,index,width):
    if index+width >= len(array) or index-width+1 < 0:
        return True
    if array[index-width+1] != array[index+width]:
        return False
    return isPalindrome(array,index,width+1)

def analysePattern(pattern,multiplyer=1):
    nReflexions = 0
    pairsIndex = pairs(pattern)
    #print(pairsIndex)
    for pair in pairsIndex:
        if isPalindrome(pattern,pair,1):
            #print(str(pair)+"is a palindrome")
            nReflexions += multiplyer*(pair+1)
    return nReflexions

def patternToNumber(pattern):
    #print([line.strip().replace('.','0').replace('#','1') for line in pattern])
    row = [int(line.strip().replace('.','0').replace('#','1'),2) for line in pattern]
    column = ['' for _ in pattern[0]]
    for i in range(len(pattern[0])):
        for line in pattern:
            column[i] += line.strip()[i]
    #print(column)
    column = [int(col.replace('.','0').replace('#','1'),2) for col in column]
    return row, column

def part1():
    totalPatterns = 0
    with open('inputs/day13.txt') as file:
        pattern = []
        for line in file: 
            if line == '\n':
                #print(pattern)
                rows, cols = patternToNumber(pattern)
                #print(rows,cols)
                totalPatterns += analysePattern(cols)
                totalPatterns += analysePattern(rows,100)
                pattern = []
                continue
            pattern.append(line.strip())
        #print(pattern)
        rows, cols = patternToNumber(pattern)
        #print(rows,cols)
        totalPatterns += analysePattern(cols)
        totalPatterns += analysePattern(rows,100)
    print(totalPatterns)
    return

part1()
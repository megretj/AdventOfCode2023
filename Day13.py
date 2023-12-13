import re 

def analysePattern(pattern):
    print(pattern)
    return 0

def part1():
    totalPatterns = 0
    with open('inputs/examples/day13.txt') as file:
        pattern = []
        for line in file: 
            if line == '\n':
                totalPatterns += analysePattern(pattern)
                pattern = []
                continue
            pattern.append(line.strip())
        totalPatterns += analysePattern(pattern)  
    print(totalPatterns)
    return

part1()
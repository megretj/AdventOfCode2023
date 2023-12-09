# For part 2, if bruteforcing doesn't work after 5 min (ok, didn't), find the number of steps of each beggining node 
# until it loops back to itself and nSteps%lenInstr == 0. In that interval, you will find
# all the nSteps of ending in Z. Then, you need to find a number that is present in all of 
# the arrays of each individual starting node modulo the number of steps that node needed to loop back. 
# But maybe this will take a lot of space.
# Turns out all loops are of the size of the instruction and there is only one final point per loop. 

import re
import math

def navigate(instructions, plan):
    nSteps = 0
    current = 'AAA'
    lenInstr = len(instructions)
    while current != 'ZZZ':
        #print(current)
        current = plan[current][int(instructions[nSteps%lenInstr])]
        nSteps+=1
    return nSteps

def endPos(posList):
    for position in posList:
        if position[-1] != 'Z':
            return False
    return True

def navigate2(instructions, plan): # Bruteforce version
    nSteps = 0
    lenInstr = len(instructions)
    current = [key for key in plan.keys() if key[-1]=='A']
    print(current)
    while not endPos(current):
        for i,branch in enumerate(current):
            current[i] = plan[current[i]][int(instructions[nSteps%lenInstr])]
        nSteps +=1
    return nSteps

def navigate3(instructions, plan):
    solution = []
    current = [key for key in plan.keys() if key[-1]=='A']
    lenInstr = len(instructions)
    print(current)
    for i,branch in enumerate(current):
        print(branch)
        nSteps = 0
        while branch[-1]!='Z':
            branch = plan[branch][int(instructions[nSteps%lenInstr])]
            nSteps+=1
        print(nSteps)
        solution.append(nSteps)
    return math.lcm(solution[0],solution[1],solution[2],solution[3],solution[4],solution[5])

def stopPoints(instructions, plan, startingPos):
    nSteps = 0
    stepsSolution = []
    lenInstr = len(instructions)
    current = startingPos
    print(lenInstr)
    while current != startingPos or nSteps%lenInstr != 0 or nSteps==0:
        current = plan[current][int(instructions[nSteps%lenInstr])]
        nSteps +=1
        if current[-1] == 'Z':
            stepsSolution.append(nSteps)
    return stepsSolution

def part1():
    with open('inputs/day8.txt') as file:
        instructions = file.readline().replace('L','0').replace('R','1').strip()
        _ = file.readline()
        plan = {}
        for line in file: 
            origin, left, right = [point for point in re.findall('\w{3}',line)]
            plan[origin] = [left, right]
    #print(plan)
    ### Change to navigate for part 1
    nSteps = navigate3(instructions,plan)
    print(nSteps)
    return nSteps

part1()
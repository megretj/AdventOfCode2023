import re
import time

# Observations: 
# reducing neighboring dots to a single dot won't change anything.
# memoization could be a good optimizaiton but it needs to be done right.

memory = {}

def rowIsValid(row,cgroups):
    defect_groups = re.finditer(pattern=r'\#+', string=row)
    groupsLengths = [group.end()-group.start() for group in defect_groups]
    #print(groupsLengths)
    if groupsLengths == cgroups:
        return 1
    return 0

def insertIntoUnknowns(n,a,start):
    # if (n,len(a)) in memory.keys():
    #     return memory[(n,len(a))]
    if n == 0:
        return [''.join(a)]
    if n == (len(a)-start):
        a[start] = '#'
        return insertIntoUnknowns(n-1,a,start+1)
    aprime = a[:]
    a[start] = '#'
    return [insertIntoUnknowns(n-1,a,start+1),insertIntoUnknowns(n,aprime,start+1)]

def flatten_nested_structure(nested_structure):
    result = []
    def flatten_helper(structure):
        for item in structure:
            if isinstance(item, (list, tuple)):
                flatten_helper(item)
            else:
                result.append(item)
    if len(nested_structure) ==1:
        return nested_structure
    flatten_helper(nested_structure)
    return result

def insertAndCheckIntoUnknowns(n,a,start,cgroups,unknown_indices):# Problem now is that a is no longer just '.'
    if n == 0:
        return rowIsValid(''.join(a),cgroups)
    if n == (len(unknown_indices)-start):
        a[unknown_indices[start]] = '#'
        return insertAndCheckIntoUnknowns(n-1,a,start+1,cgroups,unknown_indices)
    aprime = a[:]
    a[unknown_indices[start]] = '#'
    return insertAndCheckIntoUnknowns(n-1,a,start+1,cgroups,unknown_indices)+insertAndCheckIntoUnknowns(n,aprime,start+1,cgroups,unknown_indices)

def part1():
    totalConfigs = 0
    t = time.time()
    with open('inputs/day12.txt') as file:
        for line in file:
            rowString, cgroupsString = line.strip().split(" ")
            row = [symbol for symbol in rowString]
            cgroups = [int(group) for group in cgroupsString.split(',')]
            # unknownGroups = re.findall('[#\?]+',rowString)
            # print(unknownGroups)
            #print(rowString)
            #print(cgroups)
            # Start by indexing the ?
            unknown_chars = re.finditer(pattern=r'\?', string=rowString)
            unknown_indices = [number.start() for number in unknown_chars]
            # nunknown = len(unknown_indices)
            defects_total = sum(cgroups)
            defects_currently = len(re.findall('#',rowString))
            defects_needed = defects_total-defects_currently
            #empty = ['.' for _ in range(nunknown)]
            nOfChoices = insertAndCheckIntoUnknowns(defects_needed,row[:],0,cgroups,unknown_indices)
            #print(rowString,cgroups,nOfChoices)
            totalConfigs += nOfChoices
            # if not ((defects_needed,nunknown) in memory.keys()):
            #     memory[(defects_needed,nunknown)] = allChoices
            #print(allChoices)

            #print(allChoices)
            """ allChoices = flatten_nested_structure(insertIntoUnknowns(defects_needed,empty,0))
            filledRow = row[:]
            for choice in allChoices:
                #print(choice)
                filledRow = row[:]
                for emptyIndex,rowIndex in enumerate(unknown_indices):
                    filledRow[rowIndex] = choice[emptyIndex]
                #print(filledRow)
                if rowIsValid(''.join(filledRow),cgroups):
                    totalConfigs+= 1 """
    print(totalConfigs)
    print(time.time()-t)
    return

def part2():
    totalConfigs = 0
    t = time.time()
    with open('inputs/examples/day12.txt') as file:
        for line in file:
            rowString, cgroupsString = line.strip().split(" ")
            rowString = (rowString + '?')*4 + rowString
            cgroupsString= (cgroupsString+',')*4 + cgroupsString
            print(rowString,cgroupsString)
            row = [symbol for symbol in rowString]
            cgroups = [int(group) for group in cgroupsString.split(',')]
            unknown_chars = re.finditer(pattern=r'\?', string=rowString)
            unknown_indices = [number.start() for number in unknown_chars]
            defects_total = sum(cgroups)
            defects_currently = len(re.findall('#',rowString))
            defects_needed = defects_total-defects_currently
            nOfChoices = insertAndCheckIntoUnknowns(defects_needed,row[:],0,cgroups,unknown_indices)
            totalConfigs += nOfChoices
    print(totalConfigs)
    print(time.time()-t)
    return

part2()
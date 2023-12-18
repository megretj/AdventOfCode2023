import re
from tqdm import tqdm

def fileToArray(path):
    array = []
    with open(path) as file:
        for line in file:
            temp = []
            for symbol in line.strip():
                temp.append(symbol)
            array.append(temp[:])
    return array

def printImage(image):
    outputString = ''
    for row in image:
        rowString = ''
        for pixel in row:
            rowString += str(pixel)
        outputString += rowString + '\n'
    return outputString

# define [left, right, down, up]
directions = ['right', 'left', 'down', 'up']
directions_to_coordinates = [[1,0],[-1,0],[0,1],[0,-1]]
directionOrder ={'right':0, 'left':1, 'down': 2, 'up': 3}
directionsToExplore = {'.': [[0],[1],[2],[3]],'|':[[2,3],[2,3],[2],[3]], '-':[[0],[1],[0,1],[0,1]], '\\':[[2],[3],[0],[1]], '/': [[3],[2],[1],[0]]}

# add constraint that if dir in markedmapdir, then stop. 
def explore(dir,x,y,map,markedmap,markedmapdir):
    if y >= len(map) or y < 0 or x >= len(map[0]) or x < 0:
        return markedmap, markedmapdir
    if dir in markedmapdir[y][x]:
        return markedmap, markedmapdir
    markedmap[y][x] = 1
    markedmapdir[y][x].append(dir)
    if map[y][x] == '.':
        nextx = x + directions_to_coordinates[directionOrder[dir]][0]
        nexty = y + directions_to_coordinates[directionOrder[dir]][1]
        return explore(dir,nextx,nexty,map,markedmap,markedmapdir)
    for direction in directionsToExplore[map[y][x]][directionOrder[dir]]:
        nextx = x + directions_to_coordinates[direction][0]
        nexty = y + directions_to_coordinates[direction][1]
        markedmap, markedmapdir = explore(directions[direction],nextx,nexty,map,markedmap, markedmapdir)
    return markedmap, markedmapdir

def part1():
    map = fileToArray('inputs/day16.txt')
    markedmap = [[0 for _ in row] for row in map]
    markedmapdir = [[[] for _ in row] for row in map]
    markedmap, markedmapdir = explore('right',0,0,map,markedmap, markedmapdir)
    print(printImage(markedmap))
    total = 0
    for row in markedmap:
        total += sum(row)
    print(total)
    return

def exploreNext(toExplore,map):
    x,y,dir = toExplore
    candidates = set()
    for direction in directionsToExplore[map[y][x]][directionOrder[dir]]:
        nextx = x + directions_to_coordinates[direction][0]
        nexty = y + directions_to_coordinates[direction][1]
        candidates.add((nextx,nexty,directions[direction]))
    # print(candidates)
    return candidates

def part1while(start = (0,0,'right')):
    map = fileToArray('inputs/day16.txt')
    memory = set()
    beenMemory = set()
    next = {start}
    while len(next)>0:
        # print(next)
        nxt = next.pop()
        x = nxt[0]
        y = nxt[1]
        if y >= len(map) or y < 0 or x >= len(map[0]) or x < 0:
            continue
        if nxt in memory:
            continue
        if not (nxt[0],nxt[1]) in beenMemory:
            beenMemory.add((nxt[0],nxt[1]))
        memory.add(nxt)
        next = next.union(exploreNext(nxt,map))
    # print(beenMemory)
    # print(len(beenMemory))
    return len(beenMemory)

def part2():
    maximumYet = 0
    map = fileToArray('inputs/day16.txt')
    for i in tqdm(range(len(map))):
        candidate = part1while((0,i,'right'))
        if maximumYet < candidate:
            maximumYet = candidate
        candidate = part1while((len(map[0])-1,i,'left'))
        if maximumYet < candidate:
            maximumYet = candidate
    for j in tqdm(range(len(map[0]))):
        candidate = part1while((j,0,'down'))
        if maximumYet < candidate:
            maximumYet = candidate
        candidate = part1while((j,len(map)-1,'up'))
        if maximumYet < candidate:
            maximumYet = candidate
    print(maximumYet)
    return


part2()

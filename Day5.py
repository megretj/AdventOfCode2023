import re

# function f that returns an array representing the maps. 
# Would work for small array but here indices go up to a billion. 
# So better to build an array of intervals and a shift 
# 50 98 2
# a b c
# First would be the interval [98,99] with shift [-48]
# Second would be the interval [b,b+c-1] with shift [a-b] (we just take an array [b,b+c-1, a-b])
# Then given a number from the domain of f, we look if it is in the interval for every interval.
# if so, then apply shift
# if not, abbandon the number

def test():
    dict = {}
    dict['a'] = []
    dict['a'] = [[0]]
    print(dict)
    dict['a'].append([2])
    print(dict.items())
    for a,b in dict.items():
        print(a,b)
    return 

def lineToArray(line, reverse = False):
    if not reverse:
        a, b, c = re.findall(pattern='\d+', string=line)
    else:
        b, a, c = re.findall(pattern='\d+', string=line)
    return [int(b),int(b)+int(c)-1,int(a)-int(b)]

def checkSeed(map, seed):
    for range in map:
        if range[0]<= seed and seed <= range[1]:
            return seed + range[2]
    return seed

def returnCoSeed(inverseDict, coseed):
    for mapIndex in range(6,-1,-1):
        map = inverseDict[mapIndex]
        coseed = checkSeed(map,coseed)
    return coseed

def inSeed(seedsRanges,seed):
    for seedRange in seedsRanges:
        if seedRange[0] <= seed and seed <= seedRange[1]:
            return True


def part2():
    with open('inputs/day5.txt') as f:
        _, seeds = f.readline().strip().split(":")
        seedsArrayRange = re.findall(pattern='\d+', string=seeds)
        dict = {}
        inverseDict = {}
        lastMap = -1
        for index,line in enumerate(f):
            line = line.strip()
            if line=="":
                continue
            match = line.find(r" map")
            if match > -1:
                #lastMap = line[:match]
                lastMap+=1
                dict[lastMap] = []
                inverseDict[lastMap] = []
                continue
            dict[lastMap].append(lineToArray(line))
            inverseDict[lastMap].append(lineToArray(line, reverse = True))
        #print(dict)
        #print(inverseDict)
        #print(seedsArrayRange)
        seedsRanges = []
        for i in range(0,len(seedsArrayRange)-1,2):
            seedsRanges.append([int(seedsArrayRange[i]),int(seedsArrayRange[i])+int(seedsArrayRange[i+1])-1])
        print(seedsRanges)
        # an idea could be to start from zero in the co-domain and look for the first number in the domain.
        # To get a better intuition maybe see how numbers are mapped from codomain to domain. 
        # Becaus it's probably in chunks and we may be able to take advantage of this.
        # This is really bad but I got lucky that the things are really chunky 
        # oing by jumps of 100 got me close to the smallest.
        for i in range(0,78775051,50):
            if inSeed(seedsRanges,returnCoSeed(inverseDict,i)):
                print("Your solution is around"+str(i))
                break
            #if i%100000 == 0:
            #    print(i)
        # seedsEvolution = {'coseeds':list(range(0,10000))}
        # previousCategory = 'coseeds'
        # for mapIndex in range(lastMap,-1,-1):
        #     map = inverseDict[mapIndex]
        #     seedsEvolution[mapIndex] = []
        #     for seed in seedsEvolution[previousCategory]:
        #         seedsEvolution[mapIndex].append(checkSeed(map,seed))
        #     previousCategory = mapIndex
        # print(seedsEvolution)
        # for j, seed in enumerate(seedsEvolution[0]):
        #     for seedRange in seedsRanges:
        #         if seedRange[0] <= seed and seed <= seedRange[1] or j%1000==0:
        #             print("FOUND THE SEED " + str(seed) +" FROM COSEED " + str(seedsEvolution['coseeds'][j]))
        #             break
        return "finished"
    #     seedsEvolution = {'seeds':[]}
    #     for i in range(0,len(seedsArrayRange)-1,2):
    #         for j in range(int(seedsArrayRange[i]),int(seedsArrayRange[i])+int(seedsArrayRange[i+1])):
    #             seedsEvolution['seeds'].append(j)
    #     print(seedsEvolution['seeds'])
    #     print(len(seedsEvolution['seeds']))
    #     previousCategory = 'seeds'
    #     for mapName, map in dict.items():
    #         seedsEvolution[mapName] = []
    #         for evolution in seedsEvolution[previousCategory]:
    #             seedsEvolution[mapName].append(checkSeed(map,evolution))
    #         previousCategory = mapName
    # return min(seedsEvolution[mapName])

def part1():
    with open('inputs/examples/day5.txt') as f:
        _, seedsString = f.readline().strip().split(":")
        seedsArray = re.findall(pattern='\d+', string=seedsString)
        lastMap = ""
        dict = {}
        ### For part 1 ######
        # seedsEvolution = {}
        # seedsEvolution['seeds'] = []
        # for seed in seedsArray:
        #     seedsEvolution['seeds'].append(int(seed))
        #####################
        ### For part 2 ######
        seedsEvolution = {'seeds':[]}
        for i in range(0,len(seedsArray)-1,2):
            for j in range(int(seedsArray[i]),int(seedsArray[i])+int(seedsArray[i+1])):
                seedsEvolution['seeds'].append(j)
        ### still pt. 2 #####
        seedsEvolution['seeds'] = [82]
        #####################
        for index,line in enumerate(f):
            match = line.strip().find(r" map")
            if line.strip()=="":
                continue
            if match > -1:
                #print("index "+ str(index) + ", "+line.strip())
                lastMap = line.strip()[:match]
                dict[lastMap] = []
                continue
            dict[lastMap].append(lineToArray(line.strip()))
        #print(dict)
        previousCategory = 'seeds'
        for mapName, map in dict.items():
            seedsEvolution[mapName] = []
            for evolution in seedsEvolution[previousCategory]:
                image = checkSeed(map,evolution)
                seedsEvolution[mapName].append(image)
            previousCategory = mapName
        print(seedsEvolution)
    return min(seedsEvolution[mapName])

#test()
print(part1())
print(part2())
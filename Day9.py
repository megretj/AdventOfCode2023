import re 

def isAllZeros(sequence):
    for i in sequence:
        if i != 0:
            return False
    return True

def nextSequence(sequence):
    nextSequence = []
    previous = sequence[0]
    for i in sequence[1:]:
        nextSequence.append(i-previous)
        previous = i
    return nextSequence

def part2():
    total_prediction = 0
    with open('inputs/day9.txt') as file:
        for line in file:
            sequences = []
            sequences.append([int(point) for point in re.findall(r'-?\d+',line)]) 
            #print(sequences)
            while not isAllZeros(sequences[-1]):
                sequences.append(nextSequence(sequences[-1]))
            #print(sequences)
            prediction = [0]
            for sequence in reversed(sequences[:-1]):
                #print(sequence)
                prediction.append(sequence[0]-prediction[-1])
            #print(prediction)
            total_prediction += prediction[-1]
    print(total_prediction)
    return total_prediction

def part1():
    total_prediction = 0
    with open('inputs/day9.txt') as file:
        for line in file:
            sequences = []
            sequences.append([int(point) for point in re.findall(r'-?\d+',line)]) 
            #print(sequences)
            while not isAllZeros(sequences[-1]):
                sequences.append(nextSequence(sequences[-1]))
            #print(sequences)
            prediction = [0]
            for sequence in reversed(sequences[:-1]):
                #print(sequence)
                prediction.append(sequence[-1]+prediction[-1])
            #print(prediction)
            total_prediction += prediction[-1]
    print(total_prediction)
    return total_prediction

# part1()
part2()
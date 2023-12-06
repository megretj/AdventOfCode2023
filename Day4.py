import re
import numpy as np

def part2():
    noc = sum(1 for _ in open('inputs/day4.txt'))
    numOfCards = np.ones(noc)
    with open('inputs/day4.txt') as file:
        for index,line in enumerate(file):
            counter = 0
            _,card = line.split(":")
            winning, have = card.split("|")
            winning_numbers = re.findall(pattern='\d+', string=winning)
            current_numbers = re.findall(pattern='\d+', string=have)
            for number in current_numbers:
                for win in winning_numbers:
                    if number == win:
                        counter += 1
                        break
            #print("index "+ str(index)+" counter "+ str(counter))
            #print(numOfCards)
            for j in range(index+1,min(index+counter+1,noc)):
                numOfCards[j] += numOfCards[index]

    return sum(numOfCards)


def part1():
    total = 0
    with open('inputs/day4.txt') as file:
        for line in file:
            counter = -1
            _,card = line.split(":")
            winning, have = card.split("|")
            winning_numbers = re.findall(pattern='\d+', string=winning)
            current_numbers = re.findall(pattern='\d+', string=have)
            for number in current_numbers:
                for win in winning_numbers:
                    if number == win:
                        counter += 1
                        break
            if counter > -1:
                total += 2**counter
    return total

print(part2())
import re

def part1():
    total = 0
    with open('inputs/day4.txt') as file:
        for line in file:
            counter = 0
            _,card = line.split(":")
            winning, have = card.split("|")
            winning_numbers = re.findall(pattern='\d+', string=winning)
            current_numbers = re.findall(pattern='\d+', string=have)
            for number in current_numbers:
                # compare
                if similar: 
                    increase counter

            total += 2**counter
    return total

part1()
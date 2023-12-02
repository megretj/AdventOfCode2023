import re

def register_line(line):
    game_array = [0,0,0]
    for i,colour in enumerate(['red','green','blue']):
        matches = re.findall('(\d+)\ {}'.format(colour), line)
        if not matches == []:
            game_array[i] = int(matches[0])
    return game_array

def check_game(game):
    maximums = [12,13,14]
    for i,g in enumerate(game):
        if g - maximums[i]>0:
            print(game)
            print(maximums)
            return False
    return True

def power(min_set):
    tot = 1
    for i in min_set:
        tot *= i
    return tot

def part2():
    total = 0
    with open('inputs/day2.txt') as file:
        for line in file:
            min_set = [0,0,0]
            index_string, game_string = line.split(':')
            game_index = re.findall('\d+',index_string)[0]
            game_string_array = game_string.split(';')
            for game in game_string_array:
                for i,n in enumerate(register_line(game)):
                    if n > min_set[i]:
                        min_set[i]=n
            total += power(min_set)
    return total


def part1():
    total = 0
    with open('inputs/day2.txt') as file:
        for line in file:
            record = True
            index_string, game_string = line.split(':')
            game_index = re.findall('\d+',index_string)[0]
            game_string_array = game_string.split(';')
            for game in game_string_array:
                print("index " + game_index+ ", games: "+ str(game))
                if not check_game(register_line(game)):
                    record = False
            if record == True:
                total += int(game_index)

    print(total)

print(part2())


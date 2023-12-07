# Strategy is simple: import all the lines and place them, sorted, in a list or dictionnary as you go. Use binary sort.
# Once sorted, ez.
import re

def cardValue(cardString):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    strength = 1
    for card in cards:
        strength = max(strength,cardString.count(card))
    #print(cardString +" strength "+ str(strength))
    return strength

def part1():
    with open('inputs/examples/Day7.txt') as file:
        cards = {}
        for line in file:
            card, bet = line.split(" ")
            cards[card] = int(bet)
        print(cards)
        cardValue(list(cards.keys())[0])
        print(sorted(cards, key=lambda cards:cardValue(cards)))
    return

part1()

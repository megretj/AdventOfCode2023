# Strategy is simple: import all the lines and place them, sorted, in a list or dictionnary as you go. Use binary sort.
# Once sorted, ez.
import re
alphabet = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
alphabet2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def cardValue(cardString):
    strength = 1
    nPairs = 0
    for card in alphabet:
        if cardString.count(card) == 2:
            nPairs+=1
        strength = max(strength,cardString.count(card))
    #print(cardString +" strength "+ str(strength))
    return strength*10+nPairs

def cardValue2(cardString):
    strength = 1
    nPairs = 0
    for card in alphabet2[:-1]:
        if cardString.count(card) == 2:
            nPairs+=1
        strength = max(strength,cardString.count(card))
    
    nJokers = cardString.count('J')
    strength = min(strength+nJokers,5)
    if strength == 3 and nPairs == 1 and nJokers == 0:# Full house 
        return strength+.5
    if strength == 3 and nPairs == 2:# Full house
        return strength+.5
    if strength == 2 and nPairs > 1:
        return strength+.5
    #print(cardString +" strength "+ str(strength))
    return strength

def part1():
    total = 0
    with open('inputs/day7.txt') as file:
        hands = {}
        for line in file:
            hand, bet = line.split(" ")
            hands[hand] = int(bet)
        # print(hands)
        ### Part 1 ###
        # sortedHands = sorted(hands, key=lambda hands:(cardValue(hands),[len(alphabet)-alphabet.index(card) for card in hands]))
        ##############
        ### Part 2 ###
        sortedHands = sorted(hands, key=lambda hands:(cardValue2(hands),[len(alphabet2)-alphabet2.index(card) for card in hands]))
        ##############
        
        strength = {}
        for hand in sortedHands:
            strength[hand] = cardValue2(hand)
        print(strength)
        results = sum((i+1) * hands[hand] for i, hand in enumerate(sortedHands))
        print(results)
    return

part1()

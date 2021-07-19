# def die1():
#     die1 = ["axe", "gold_arrow", "helmet", "gold_hand", "shield", "axe"]
#     return (random.choice(die1))

# def die2():
#     die2 = ["axe", "arrow", "gold_hand", "helmet", "gold_shield", "axe"]
#     return (random.choice(die2))

# def die3():
#     die3 = ["axe", "hand", "gold_helmet", "shield", "gold_arrow", "axe"]
#     return (random.choice(die3))

setOfDice = [["1axe", "1gold_arrow", "1helmet", "1gold_hand", "1shield", "1axe"],
                ["2axe", "2arrow", "2gold_hand", "2helmet", "2gold_shield", "2axe"],
                ["3axe", "3hand", "3gold_helmet", "3shield", "3gold_arrow", "3axe"],
                ["4axe", "4gold_hand", "4gold_helmet", "4axe", "4shield", "4arrow"],
                ["5axe", "5hand", "5helmet", "5gold_arrow", "5gold_shield", "5axe"],
                ["6axe", "6hand", "6arrow", "6gold_helmet", "6gold_shield", "6axe"]]

import random

def rollDice(numOfDie):
    dieToRoll = setOfDice[numOfDie]
    print("Your die roll is " + random.choice(dieToRoll))

availableDice = [0,1,2,4]
submittedDice = [3,5]
    
for x in availableDice:
    rollDice(x)
import random

class Dice:

    def __init__(self, player):
        self.player = player

    faces = ["arrow", "axe", "hand", "helmet", "shield", "gold_arrow", "gold_shield", "gold_helmet"]
    setOfDice = [["0axe", "0gold_arrow", "0helmet", "0gold_hand", "0shield", "0axe"],
                ["1axe", "1arrow", "1gold_hand", "1helmet", "1gold_shield", "1axe"],
                ["2axe", "2hand", "2gold_helmet", "2shield", "2gold_arrow", "2axe"],
                ["3axe", "3gold_hand", "3gold_helmet", "3axe", "3shield", "3arrow"],
                ["4axe", "4hand", "4helmet", "4gold_arrow", "4gold_shield", "4axe"],
                ["5axe", "5hand", "5arrow", "5gold_helmet", "5gold_shield", "5axe"]]
    availableDice = [0,1,2,3,4,5]
    confirmedDice = []
    
    
    def rollDice(self, numOfDie):
        dieToRoll = Dice.setOfDice[numOfDie]
        return random.choice(dieToRoll)



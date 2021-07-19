from Dice import Dice
from Player import Player

class Game:

    def __init__(self):
        super().__init__()

    def game():
        player1Dice = Dice("Matt")
        print(player1Dice.availableDice)
        print(player1Dice.confirmedDice)
        for x in player1Dice.availableDice:
            print(player1Dice.rollDice(x))

        diceToKeep = input("Select which dice you would like to keep: ")
        
        player1Dice.availableDice.pop(diceToKeep)
        player1Dice.confirmedDice.append(diceToKeep)

        print(player1Dice.availableDice)
        print(player1Dice.confirmedDice)

        for x in player1Dice.availableDice:
            print(player1Dice.rollDice(x))

        print(player1Dice.availableDice)
        print(player1Dice.confirmedDice)


    def main():
        print("roll your dice")
        Game.game()

Game.main()

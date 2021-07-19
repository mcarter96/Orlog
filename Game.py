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
        
        print(diceToKeep)


    def main():
        print("roll your dice")
        Game.game()

if __name__ == "__main__":
    Game.main()

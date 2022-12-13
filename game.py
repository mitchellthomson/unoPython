from player import Player

class Game:
    def __init__ (self, playerOne: Player, playerTwo: Player, playerThree: Player, playerFour: Player):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.playerThree = playerThree
        self.playerFour = playerFour
        self.current_card = None
        
    def play(self):
        print("Begin")
        self.playerOne.current_card_disp(self.current_card)
        self.playerOne.hand_disp()
        self.playerOne.turn_prompt(self.current_card)
        self.playerOne.hand_disp()
        
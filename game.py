from player import Player
from helpers import clear
class Game:
    def __init__ (self, playerOne: Player, playerTwo: Player, playerThree: Player, playerFour: Player):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.playerThree = playerThree
        self.playerFour = playerFour
        self.current_card = None
        self.game_deck = None
        
    def play(self):
        clear()
        print("Begin")
        
        while not self.check_win():
            self.playerOne.current_card_disp(self.current_card)
            self.playerOne.hand_disp()
            self.playerOne.turn_prompt(self.current_card ,self.game_deck)
            self.current_card = self.playerOne.played_card
            
            clear()
            
            self.playerTwo.current_card_disp(self.current_card)
            self.playerTwo.hand_disp()
            self.playerTwo.turn_prompt(self.current_card ,self.game_deck)
            self.current_card = self.playerTwo.played_card
            
            clear()
            
            self.playerThree.current_card_disp(self.current_card)
            self.playerThree.hand_disp()
            self.playerThree.turn_prompt(self.current_card ,self.game_deck)
            self.current_card = self.playerThree.played_card
            
            clear()
            
            self.playerFour.current_card_disp(self.current_card)
            self.playerFour.hand_disp()
            self.playerFour.turn_prompt(self.current_card ,self.game_deck)
            self.current_card = self.playerFour.played_card
            
    def check_win(self):
        if len(self.playerOne.hand) == 0:
            print("Player1 wins!")
            return True
        elif len(self.playerTwo.hand) == 0:
            print("Player2 wins!")
            return True
        elif len(self.playerThree.hand) == 0:
            print("Player3 wins!")
            return True
        elif len(self.playerFour.hand) == 0:
            print("Player4 wins!")
            return True
        else:
            return False
from termcolor import colored
from card import Card

class Player:
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name
    
    def hand_disp(self):
        for card in self.hand:
            print(colored(card.get_special_card(), card.color))
            
    def turn_prompt(self):
        card = input("Pick the card to play: (format: number/name - color): ")
        while not self.card_check(card):
            print("Invalid pick a different move")
            card = input("Pick the card to play: (format: number/name - color): ")
        self.play_card(card)
        return card
    
    def card_check(self, card:str):
        for x in self.hand:
            if str(x) == card:
                return True
        return False
    
    def play_card(self, card:str):
        for x in self.hand:
            if str(x) == card:
                self.hand.remove(x)
            break
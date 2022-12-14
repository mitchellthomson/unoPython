from termcolor import colored
from card import Card


class Player:
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name
        self.played_card = None
        
    def hand_disp(self):
        for card in self.hand:
            print(colored(card.get_special_card(), card.color))
            
    def current_card_disp(self,current_card):
        c =(colored(current_card.get_special_card(), current_card.color))
        print("Current card is: " + c)
        
    def turn_prompt(self, current_card, game_deck):
        card = input("Pick the card to play: (format: number/name - color), if no play type draw to get card: ")
        while not self.card_check(card, current_card, game_deck):
            print("Invalid pick a different move")
            card = input("Pick the card to play: (format: number/name - color), if no play type draw to get card: ")
            if(card=="draw"):
                return card
            else:
                self.play_card(card)
        return card
    
    def card_check(self, card:str, current_card, game_deck):
        if card == "draw":
            self.draw_card(current_card, game_deck)
            return True
        else:
            for x in self.hand:
                if str(x) == card and ((current_card.color == x.color or current_card.number == x.number) or (current_card.color == 'magenta' or x.color == 'magenta')):
                    self.played_card = x
                    return True
        return False
    
    def play_card(self, card:str):
        for x in self.hand:
            if str(x) == card:
                self.hand.remove(x)
            break
    
    def draw_card(self, current_card, game_deck):
        self.hand.append(game_deck[0])
        game_deck.pop(0)
        self.played_card = current_card
        return True
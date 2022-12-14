from card import Card
from subprocess import call
import os


def create_deck():
    newDeck = []
    for color in ["red", "blue", "green", "yellow"]:
        for number in range(1,10):
            newDeck.append(Card(color, None, number))
        for special in ["reverse", "two", "skip"]:
            newDeck.append(Card(color, special, None))
    
    newDeck.append(Card("magenta","four",None))
    newDeck.append(Card("magenta","four",None))
    newDeck.append(Card("magenta","choose",None))
    newDeck.append(Card("magenta","choose",None))
    return newDeck

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
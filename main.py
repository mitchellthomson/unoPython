from helpers import create_deck
from card import Card
from player import Player
from game import Game
import itertools, random


def deal_cards():
    deck = create_deck()
    random.shuffle(deck)
    return deck[1:9], deck[9:17],deck[17:25], deck[25:33], deck[0], deck[33:]

a, b ,c, d, cur, g_deck= deal_cards()

player_a = Player(a, "Player A")
player_b = Player(b, "Player B")
player_c = Player(c, "Player C")
player_d = Player(b, "Player D")


g = Game(player_a, player_b, player_c, player_d)
g.current_card = cur
g.game_deck = g_deck
g.play()
# -*- coding: utf-8 -*-

import random

class Trump:
    suits = ['spade', 'club', 'heart', 'dia']
    min_num = 1
    max_num = 13

    def __init__(self) :
        self.deck = self.make_deck()

    def make_deck(self) :
        deck = []
        for suit in self.suits:
            for num in range(self.min_num, self.max_num + 1) :
                card = {'suit': suit, 'num': num}
                deck.append(card)

        random.shuffle(deck)
        return deck


    def draw(self, num) :
        cards = []
        for step in range(num) :
            cards.append(self.deck.pop(0))

        return cards




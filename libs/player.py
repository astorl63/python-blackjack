# -*- coding: utf-8 -*-

class Player:
    def __init__(self) :
        self.hands = []
    
    def push_card(self, cards) :
        for card in cards :
            self.hands.append(card)
    
    def show_hands(self) :
        for card in self.hands :
            print(card)

    def total_hands(self) :
        num = 0
        for card in self.hands :
            num += card["num"]

        return num


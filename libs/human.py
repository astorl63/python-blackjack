# -*- coding: utf-8 -*-

from player import Player

class Human(Player):
    def __init__(self) :
        super().__init__()

    def ask_draw(self) :
        is_draw = False
        response = input('draw card ? please input y/n :')

        if response == 'y' :
            is_draw = True
        
        return is_draw

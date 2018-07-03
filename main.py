# -*- coding: utf-8 -*-

# ▼簡単なブラックジャックを作る
# http: // www.othello.org/bj/
# 
# ・CPUとの一対一の戦い
# ・ユーザにカードを二枚配り、カード内容と合計値を表示する
# ・CPUにカードを配り、持っている一枚の数字を表示する
# ・ユーザがカードを引くか引かないかを入力させる
# ・引いた場合は引いた結果のカードの内訳と合計を表示する
# ・CPUの引く引かないのロジックは自由
# ・勝敗の結果を表示する

# import pdb; pdb.set_trace()

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/libs')

from trump import Trump
from human import Human
from computer import Computer

class BlackJack:
    def __init__(self, trump, human, computer) :
        self.trump = trump
        self.human = human
        self.computer = computer

    def start(self) :
        # 人間がカードを引く
        self.draw(self.human, 2)
        self.show(self.human)

        # CPUがカードを一枚引き、数字を表示してもう一枚引く
        self.draw(self.computer, 1)
        self.show(self.computer)
        self.draw(self.computer, 1)

        # 人間にもう一度引くかインプットを求める
        if self.human.ask_draw():
            self.draw(self.human, 1)
            self.show(self.human)

        # CPUが自身の手札からカードのドローを判断する
        if self.computer.gamble_draw() :
            self.draw(self.computer, 1)
            self.show(self.computer)
        
        self.judge()

    # カードを山札から引く
    def draw(self, player, num) :
        cards = self.trump.draw(num)
        player.push_card(cards)

    # プレイヤーの手札を画面に表示する
    def show(self, player) :
        print('### ' + player.__class__.__name__ + ' cards')
        player.show_hands()
    
    # 勝敗判定と結果表示
    def judge(self) :
        human = self.human.total_hands()
        computer = self.computer.total_hands()

        print('human: '+str(human))
        print('computer: '+str(computer))


# ゲームスタート
blackjack = BlackJack(Trump(), Human(), Computer())
blackjack.start()

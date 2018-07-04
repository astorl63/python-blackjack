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

from blackjack import Blackjack
from trump import Trump
from human import Human
from computer import Computer

# ゲームスタート
blackjack = Blackjack(Trump(), Human(), Computer())
blackjack.start()

"""
Q5. おみくじプログラムを作成してください。
    おみくじの結果は、大吉、中吉、小吉、凶の4種類とします。
    1: 大吉
    2: 中吉
    3: 小吉
    4: 凶
    とします。

    おみくじの結果は、ランダムに決定してください。
    ランダムな整数値を取得するには、randomモジュールのrandint関数を使用します。

    また、おみくじの結果を表示する際に、おみくじの結果の前に「あなたの運勢は」と表示してください。
"""

import random

result = random.randint(1, 4)  # 1~4のランダムな整数を取得

'''
if result == 1:
    print('あなたの運勢は 大吉')
elif result == 2:
    print('あなたの運勢は 中吉')
elif result == 3:
    print('あなたの運勢は 小吉')
else:
    print('あなたの運勢は 凶')
'''



luck = ""
if result == 1:
    luck = "大吉"
elif result == 2:
    luck = "中吉"
elif result == 3:  
    luck = "小吉"
else:
    luck = "凶"

print(f"あなたの運勢は {luck}です")

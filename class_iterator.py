#カウントダウン
class CountDown:
    def __init__(self, start):
        self.number =start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number<=0:
            raise StopIteration
        self.number -= 1
        return self.number + 1

count_down = CountDown(5)

for count in count_down:
    print(count)


#残金内でランダムに寿司を握る

import random

SUSHI_NETA =[
    {"name": "まぐろ赤身", "price":100},
    {"name": "えんがわ", "price":100},
    {"name": "いくら", "price":200},
    {"name": "サーモン", "price":200},
    {"name": "玉子", "price":100},
    {"name": "えび", "price":200},
    {"name": "たこ", "price":200},
    {"name": "大トロ", "price":400},
    {"name": "うに", "price":400},
]

class Itamae:
    def __init__(self, deposit):
        print(f"{deposit}円の範囲でなにか握ります。")
        self.deposit = deposit
    
    def __iter__(self):
        return self
    def __next__(self):
        #残金ないで握れるネタのリストを作る
        neta_list = [neta for neta in SUSHI_NETA 
                    if neta["price"] <= self.deposit]
        
        #ネタがなければ修了
        if len(neta_list) == 0:
            print("握れるネタがありません。")
            raise StopIteration
        
        #ネタをランダムに選ぶ
        neta = random.choice(neta_list)
        self.deposit -= neta["price"]
        return neta
    
itamae = Itamae(1560)
for neta in itamae:
    print(f"{neta['name']}は{neta['price']}円です。残金は{itamae.deposit}円です。")
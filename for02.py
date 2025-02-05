#年齢ガチャ
import random

age = int(input('何歳ですか？\n'))
#break ループを終了させる
for _ in range(age):
    result = random.randint(1, 10)
    
    if result > 9:
        print(f"{result} \tレアアイテム")
        break
    else:
        print(f"{result} \tノーマルアイテム")
        
#continueでスープ処理をスキップしてブロックの先頭へ戻る
#例1奇数のみの出力
for _ in range(20):
    if _ % 2 == 0:
        continue
    print(_)
    

#例2レアガチャのみ表示
gacha_list = ["common", "rare", "common", "rare", "common", "レア"]

for gacha in gacha_list:
    if gacha == "common":
        continue
    print(gacha)

#else ループ修了時になにか処理をする    breakがあればそこでおわり
for i in range(10):
    print(i)
else:
    print("終了")

for x in range(10):
    print(x)
    if x == 5:
        break
else:
    print("end")
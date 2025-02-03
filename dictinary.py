colors = {
    "red":"赤",
    "blue":"青",
    "green":"緑",
}

print(colors["red"])

#dict関数
colors2 = dict(gray="グレー", black="黒", white="白")
print(colors2["gray"])


yellow = ("yellow", "黄")
pink = ("pink", "ピンク")
orange =("orange", "オレンジ")
colors3 = dict([yellow, pink, orange])
print(colors3)

print(colors.get('blue'))
print(colors.get('brown', 'ないです'))

#リストへの追加（上書き）
animals = {
    "dog":"犬",
    "cat":"猫",
    "mouse":"ねずみ",
}
animals["rabbit"]= "うさぎ"
print(animals.get('rabbit' ,'見つかりません'))

animals.update({"panda":"パンダ", "bear":"熊"})
print(animals)

animals2 = dict(cow="牛", horse="馬")
animals.update(animals2)
print(animals)

#追加しようとする要素が存在していた場合上書きしない方法
#setdefault
animals2.setdefault("cow","うし")
print(animals2)

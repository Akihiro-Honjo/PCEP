#関数とメソッド
colors = dict(red="赤", blue="青", green="緑", yellow="黄")

#len(要素数)
print(len(colors))

#del(要素の削除)存在しない場合はkeyError
del colors["yellow"]
print(colors)

#key 辞書内のすべてのキーを含むdict_keysオブジェクトを返す
print(colors.keys())

#values
print(colors.values())

#items
for key, value in colors.items():
    print(key, value)
print(colors.items())

#pop() 指定したkeyに対応する値を返し、辞書から要素を削除する
print(colors.pop("red"))
print(colors)

#clear()すべての要素を削除する
colors.clear()
print(colors)

colors2 = dict(gray="グレー", black="黒", white="白")

#in演算子 指定したkeyが含まれるかどうか
#valueを使う場合は .values

result = "gray" in colors2
print(result)

result = "黒" in colors2.values()
print(result)

result = "orange" in colors2
print(result)
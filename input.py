name = input("あなたの名前を入力してください")
print("こんにちは", name)

#str型
age = input("あなたの年齢を入力してください")
age = int(age)
print(age + 1)

name = input("名前を入力してください")
print(f'こんにちは{name}さん')

age = int(input("あなたは何歳ですか？"))#inputはすべて文字列になる。intで整数型に変換
print(f"あなたは来年{age + 1}歳にですね")
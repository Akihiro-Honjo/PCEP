#内包表記

#リスト内包表記[式 for 要素 in イテラブル if 条件式]

#0から9までの二乗
'''
squares = []
for _ in range(10):
    squares.append(_**2)
print(squares)
'''
squares = [x**2 for x in range(10)]
print(squares)

#文字列を大文字にする
fruits_list = ['apple', 'banana', 'orange', 'grape']
fruits_upper =[fruit.upper() for fruit in fruits_list if len(fruit) ==5] #5文字だけのとき
print(fruits_upper)

#指定した文字列で始まるものだけのリストを作る
#startswith()文字列が指定した文字列で始まるかを判定するメソッド
TOKYO = "東京都"
address = ["東京都千代田区", "千葉県船橋市", "東京都杉並区", "埼玉県大宮市", "東京都町田市"]
tokyo_town = [town.replace(TOKYO, "") for town in address if town.startswith(TOKYO)] #.replaceは文字列の置換
print(tokyo_town)



#セット内包表記
#{式 for 要素 in イテラブル if 条件式}

number_list = [10, 20, 10, 100, 200, 400, 100, 200]

over_100_set = {x for  x in number_list if x >= 100}
print(over_100_set)

#ジェネレータ式
my_tuple = tuple((x for x in range(10)))
print(my_tuple)
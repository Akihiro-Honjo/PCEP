#辞書内包表記
#{キー: 値 for 要素 in イテラブル if 条件式}

#2つのリストを辞書にする
e_seasons = ['spring', 'summer', 'autumn', 'winter']
j_seasons = ['春', '夏', '秋', '冬']

seasons_dict ={e:j for e,j in zip(e_seasons, j_seasons)}
print(seasons_dict)

#辞書の値をフィルタリングする
sample_dict = {"apple":1, "banana":2, "cherry":3, "orange":4 , "mango":5}
filtered_dict = {
    k:v for k, v in sample_dict.items() if v % 2 == 0
}
print(filtered_dict)

#三項演算子で値を動的に変更
number_list =list(range(1, 11))
my_dict = {num:("even" if num % 2 == 0 else "odd") for num in number_list }
print(my_dict)

#ネストした辞書内包表記を使用してリストの要素を辞書に変換する
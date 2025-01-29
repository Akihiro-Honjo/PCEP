static_langs = ['C', 'C++', 'Java', 'C#']
dynamic_langs = ['Python', 'JavaScript', 'PHP', 'Ruby']

# append メソッドを使って以下の構造、データのリストを新たに作成、表示してください。
# [['C', 'C++', 'Java', 'C#'], ['Python', 'JavaScript', 'PHP', 'Ruby']]
# (nested_lange = [static_langs, dynamic_langs] と書くこともできますがあえて)
nested_langs = [static_langs]
nested_langs.append(dynamic_langs)
print(nested_langs)

# extend メソッドを使って以下の構造、データのリストを新たに作成、表示してください。
# ['C', 'C++', 'Java', 'C#', 'Python', 'JavaScript', 'PHP', 'Ruby']
extended_langs = static_langs
extended_langs.extend(dynamic_langs)
print(extended_langs)

# pop メソッドを使って nested_langs から 要素 python を取り出し変数に格納、出力してください。
python = dynamic_langs.pop(0)
print(python)

# insert メソッドを使って extended_langs の Java の後に Swift を追加、表示してください。
extended_langs.insert(3, 'Swift')
print(extended_langs)
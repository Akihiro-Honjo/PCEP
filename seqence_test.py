languages = ['python', 'perl', 'c++', 'java', 'ruby', 'c#', 'go', 'scala', 'php', 'javascript', 'swift', 'r']
# languages から python を取り出し、表示してください。 (正のインデックスで指定)
print(languages[0])  # python

# languages から r を取り出し、表示してください。 (負のインデックスで指定)
print(languages[-1])  # r

# languages の c++ から c# までを取り出し、表示してください。 (正のインデックスでスライス)
print(languages[2:6])  # ['c++', 'java', 'ruby', 'c#']

# languages の php から swift までを取り出し、表示してください。 (負のインデックスでスライス)
print(languages[-4:-1])  # ['php', 'javascript', 'swift']

# languages の perl から scala までを取り出し、表示してください。 (正のインデックス、ステップ数2)
print(languages[1:8:2])  # ['perl', 'java', 'c#', 'scala']

# languages の先頭から go までを取り出し、表示してください。 (先頭は省略表記)
print(languages[:7])  # ['python', 'perl', 'c++', 'java', 'ruby', 'c#', 'go']

# languages の java から末尾の要素までを表示してください。 (末尾は省略表記)
print(languages[3:])  # ['java', 'ruby', 'c#', 'go', 'scala', 'php', 'javascript', 'swift', 'r']

# languages の要素を逆順にして表示してください。
print(languages[::-1])  # ['r', 'swift', 'javascript', 'php', 'scala', 'go', 'c#', 'ruby', 'java', 'c++', 'perl', 'python']

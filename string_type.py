s = """
これは
改行を含む
文字列です。
"""
print(s)

ss = "これは\n改行を含む\n文字列です。\n"
print(ss)

#Docstring(ドックストリング)
#"""で囲われた文字列は関数やクラスの説明として使われる"
def greet(name):
    """
    あいさつする関数
    :param name: 名前
    :return: なし
    """
    print(f"Hello, my name is {name}!")

greet('Taro')
print(greet.__doc__)


print('abc' + 'def')

a = 'py'
print(a + 'thon')

x = 'file'
y = "clean_%s" % x
print(y) #clean_file
# %s:文字列 %d:整数 %f:浮動小数点数を結合する

#formatメソッド
first_name = "Taro"
last_name = "Yamada"
print('Hi {} {} '.format(first_name, last_name))

greet = 'Hello {1} {0}'
print(greet.format(first_name, last_name))

pi = 3.141592653
print("円周率は{pi:.2f}です".format(pi=pi))
amount = 10000
print("支払い金額は{amount:,}円です。".format(amount=amount))
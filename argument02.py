#デフォルト値
'''
def greet(name="John"):
    print(f"Hello,{name}!")
greet("taro")
greet()

'''

#デフォルト値をミュータブル（変更可）にするときの注意点
#ミュータブルの初期値が空だった場合、２回目移行に実行したときに前回の状態が次回の初期値になる
def greet(name, name_list=[]):
    name_list.append(name)
    return name_list

names = greet('John',['jane', 'Joe', 'Jack'])
print(names) #['John','jane', 'Joe', 'Jack']

names = greet('Mary')
print(names) #['Mary']

names = greet('Bob')
print(names) #['Mary', 'Bob']

names = greet('Alice')
print(names) #['Mary', 'Bob', 'Alice]



#9
swimmer = [s * 2 for s in 'swimmer']
print(swimmer)

#10
vocab = 'exploration'
print(vocab[2:11:3])

#11 row各行のリスト1の要素を抽出する
matrix = [[2, 4, 6, 8, 10],
        [12, 14, 16, 18, 20]]

collected = [row[1] for row in matrix]

print(collected)


#14 JSON形式の文字列に。その際はダブルクォート(")を使う必要がある。
import json
x = {'name':'suzuki','data':[3,4,5]}
print(json.dumps(x))

#17
x = ['a','b','c','d','f']
print(x[:-4])

#18
cities = {"city1": "Tokyo", "city2": "Osaka", "city3": "Kyoto"}

print("出力結果: ", end="")
for k, v in cities.items():
    print(v, end=" ")
    

#19
import math
print('出力結果:')
print('円周率は%5.3fである。' % math.pi)
# %5.3fは %f：浮動小数点数（小数）を表示,.3：小数点以下3桁まで表示,5：全体の幅を最低5文字にする（必要なら空白で埋める）
#(ここでは 3.142 のようにちょうど5文字なので、空白は入りません。)


#20
class Example:
    lst = []

    def add_e_list(self, data):
        self.lst.append(data)

print('出力結果:', end=' ')
example1 = Example()
example1.add_e_list('データ1')

example2 = Example()
example2.add_e_list('データ2')

for item_data in example1.lst:
    print(item_data, end=' ')
    
    
    

#25
def hoge(title, content = 'default_content', number = 4):
    content = 'content'
    print(title, end=' ')
    print(content, end=' ')
    print(number)

hoge(title = 'title_default', content = 'None', number = 5) 


#28 removeメソッドは最初に見つかった要素を削除する
arr = [7, 2, 5, 1, 5, 6, 7, 1]
arr.remove(1)
print(arr)

#29
numbers = [3, 5, 7, 5, 5, 3, 7]
for i in range(numbers.count(5)):
    print(i, end=' ')
#numbers.count(5)でリスト内の5の数を数える（3個）。⇒for i in range(3)で0,1,2を出力する。

#32 実行結果をWatanabeにしたい
coding_school = ['Sato', 'Suzuki', 'Tanaka', 'Watanabe', 'Ito', 'Yamada']


ex_student = coding_school.pop(3)

print(ex_student)



#36
class ProgrammingSchool:
    def __init__(self, teacher, mentor):
        self.teacher = teacher
        self.mentor = mentor

ps = ProgrammingSchool('Yamada', 'Suzuki')
print(ps.teacher)
print(ps.mentor)


#40
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print('Woof!')

my_dog = Dog('Max')
print(my_dog.name)
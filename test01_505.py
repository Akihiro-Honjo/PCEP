#1
print('こんにちは!{}さん'.format('鈴木'))

#2
coding_school = ['Sato', 'Suzuki', 'Tanaka', 'Watanabe', 'Ito', 'Yamada']
coding_school.clear()
print(coding_school)

coding_school2 = ['Sato', 'Suzuki', 'Tanaka', 'Watanabe', 'Ito', 'Yamada']
del coding_school2[:]
print(coding_school2)


#3
members = {1: 'Sato', 2: 'Suzuki', 3: 'Tanaka'}
members[4] = 'Yamada'
del members[3]
print(list(members.keys()))


#5
def programming_school(teacher, *mentor):
    print(teacher)

programming_school('Sato', 'Suzuki', 'Tanaka')

#6
programming_school =  [(1, 'Sato'), (2, 'Suzuki'), (3, 'Tanaka'), (4, 'Yamada')]
ps = programming_school
ps.sort(key=lambda ps: ps[1], reverse=True)
#key=lambda ps: ps[1]で、タプルの2番目の要素を基準にソートする。
#reverse=Trueで降順にソートする。
print(ps)


#12
p = 'python'
p + 'rules'
print('1:', p)

p += 'abc'
print('2:', p)


#14
import json
x = {'name': 'suzuki', 'data' : [3, 4, 5]}
print(json.dumps(x)) #json.dumps()で辞書をJSON形式の文字列に変換する。


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


#29
numbers = [3, 5, 7, 5, 5, 3, 7]
for i in range(numbers.count(5)):
    print(i, end=' ')
    

#32
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



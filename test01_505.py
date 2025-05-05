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

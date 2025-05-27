x = 10
y = 5
print(x // y)


a = {'x': 1, 'y': 2}
print(a.get('z', 0))

for i in range(3):
    print(i, end="-")
    

text = "Python"
print(text[::-1])



print("-" *20)

a = [1, 2, 3]
b = a[:]
b[0] = 100
print(a)
print(b)


S = "Hello, world!"
print(S[7:12])#スペースもインデックスに含まれる


print(7 // 3)
print(9 / 3)
print(7 % 3)


numbers = [10,20,30,40,50,60]
result = numbers[::2]
result2 = numbers[1::6]
print(result)
print(result2)
#スライス構文[start:end:stop]


number_list = [3, 5, 7, 5, 5, 3, 7]
for i in range(number_list.count(5)):
    print(i, end=" ")
    

user1, user2, user3, user4 = '', 'yamada', 'kobayashi', 'watanabe'
chosen_user = user1 or user2 or user3 or user4
print(chosen_user)
#空文字列はFalseと評価されるため、最初の空文字列は無視され、次の'yamada'が選ばれる

s = 'jump\\nover\\nthe\wall'
print(s)
print(len(s))

names1 = ['Sato', 'Kato', 'Ishida']
names2 = ['Yamada', 'Watanabe', 'Mori']
names3 =  ['Suzuki', 'Takahashi', 'Ivanov']
output = zip(names1, names2, names3)
print(list(output))
#zip()リストを位置ごとにまとめてタプルの形にする


def outer_func():
    x = 'outer'
    def inner_func():
        nonlocal x
        x = 'inner'
        print('Inner:', x, end=' ')
    inner_func()
    print('Outer:', x, end=' ')

outer_func()


print(range(6))
#range(0, 6)

[(i, j) for i in range(3) for j in range(1, 4) if i != j]
print([(i, j) for i in range(3) for j in range(1, 4) if i != j])

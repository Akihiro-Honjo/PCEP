#10
text = "Hello, python"
for t in text:
    if t == "p":
        break
    print(t)
    
#12
num = 1

def add(a, b=10):
    num = 5
    print(a + b)

num = 2
add(num)

#13
def test(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
test("Yamada", "特技は水泳", "趣味は読書",  job="デザイナー", age=18)

#14
my_list =  ["特技は水泳", "趣味は読書"]
print(*my_list)


#15
fun = lambda a, b: a + b
print(fun(5, 2))

names = ['Tanaka', 'Sato', 'Yamada']
names.sort(key=lambda x: len(x))
print(names)


#16
pairs = [(5, 'b'), (15, 'c'), (10, 'a')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


#18
colors = ["red", "black", "green"]
more_colors = ["yellow", "white"]

colors.append("blue")
print(colors)

colors.extend(more_colors) # extend()メソッドを使用してリストを結合
print(colors)



print('--' * 20)

#19
colors2 = ['red', 'black', 'green', 'blue', 'yellow', 'white']

colors2.sort()
print(colors2)

colors2.sort(key=len)
print(colors2)


print('--' * 20)
#20
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([tuple(row[i] for row in matrix) for i in range(3)])

matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(zip(*matrix2)))


#21
users = {'Yamada': 170, 'Suzuki': 165}
users['Takayama'] = 172
print(users['Yamada'], end=',') #user['Yamada']は170を辞書から取り出す、end=''は改行しない
print(users)


#22
en = ["red", "white", "blue"]
ja = ["赤色", "白色", "青色"]
l = []

for e, j in zip(en, ja):
    l.append((e,j))

print(l)

# print([e, j for e, j in zip(en, ja)])
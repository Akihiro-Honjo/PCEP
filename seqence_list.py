
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(my_list))
print(my_list[0])

my_list[0] = 100
print(my_list)

names = ['John', 'Paul', 'George', 'Ringo']
print(names[0])# John
print(names[-1])# Ringo
print(names[-3])# Paul

#リストの作り方
my_list2 = []
my_list2.append("Bob")
my_list2.append("Tom")
my_list2.append("Ken")
my_list2.append("John")
print(my_list2)
my_list2.insert(1, "Paul")
print(my_list2)
print(my_list2[1])

even_list =[]
for number in range(1, 20):
    if number % 2 == 0:
        even_list.append(number)
        
print(even_list)

#spritメソッド
#csvファイルの読み込みなどで使う
lang = 'python, ruby, java, c++'
lang_list = lang.split(',')
print(lang_list)


string = 'Happy'
string_list = list(string)
print(string_list)

r = range(10)
print(list(r))
for _ in range(10):
    print(_)
    
s = {1, 2, 3, 4, 5}
print(s)
print(list(s))

#元のリストに追加したものを返す（元のリストは変わらない）
list = ["apple", "banana", "orange"]
neW_list = list + ["grape"]
print(list+["grape"])
print(list)
print(neW_list)

#元のリストに追加（元のリストが変わる）+=

lst = ["a", "b", "c"]
lst += ["d"]
print(lst)
print(lst*2) #繰り返し



lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst1.append(lst2) #末尾に要素を追加
print(lst1)

lst1.extend(lst2) #リストを拡張（結合）
print(lst1)

#指定した位置に要素を追加
lst3 = [7, 8, 9]
lst3.insert(0, '六') 
print(lst3)

#値を取り出す（リストからは削除される）（スクレイピングなどで使う）
fruits = ['apple', 'banana', 'orange']
banana = fruits.pop(1)
print(banana)
print(fruits)
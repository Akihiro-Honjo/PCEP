
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
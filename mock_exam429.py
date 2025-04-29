

#15
class Animal:
    legs = 4
    
    def __init__(self,name):
        self.name = name
    
tama = Animal('Tama')
pochi = Animal('Pochi')

print(tama.legs, tama.name)
print(pochi.legs, pochi.name)


#19
users = ["Tanaka", "Suzuki", "Akayama", "Miyamoto"]

copy_users = users.copy()

users.remove("Akayama")
print(users)

users.clear()
print(users)

print(copy_users)


#21
a = 7
b = 2
c = a / b
d = a // b
e = a % b
print("c:", c, "d:", d, "e:", e)
# c=a÷b, dはaをbで割った商, eはaをbで割った余り


#23
print("python\name") #python + 改行 + ame \n は「改行文字（newline）」
print("python\\name") #python\name \\ はエスケープされて、1つの \ に変換されます。
print(r"python\name") #python\name  r"..." はraw（生）文字列リテラル。


#25
num = [1, 3, 5, 7, 9]
print(num[-1])

#26
a, b = 1, 5
while a < 30:
    print(a, end=' ')
    a = a + b
    
print('-' * 10)
#28
for count in range(2): 
    print(count)
    

#31
def add(a, b=2): 
    return a + b 

print(add(1))

#32
number = 3
def add(a=5, b=number):
    print(a+b)

b=2
add()

def test(name, *b, **a):
    print(name) #"Yamada"
    for kw in a:
        print(a[kw]) # "デザイナー", 18
    for arg in b:
        print(arg) # "特技は水泳", "趣味は読書"

test("Yamada", "特技は水泳", "趣味は読書",  job="デザイナー", age=18)
# 位置引数⇒name, *b
# キーワード引数⇒**a 先に位置引数、後にキーワード引数



print("*" * 20)
#別問題
def profile(name, *hobbies, **info):
    print("名前:", name)
    for hobby in hobbies:
        print("趣味:", hobby) #可変長引数
    for key, value in info.items():
        print(f"{key}: {value}") #キーワード引数

hobby_list = ["読書", "水泳", "旅行"]
personal_info = {"年齢": 25, "職業": "エンジニア"}

profile("田中", *hobby_list, **personal_info)
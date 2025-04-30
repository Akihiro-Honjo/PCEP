

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


#36
numbers = [5, 3, 5, 1, 3, 2, 4, 3, 4, 3]

print(numbers.index(3), end=",") #最初から（インデックス0から）、3 を探す⇒1
print(numbers.index(3, 2), end=",") #インデックス 2から最後まで の間で 3 を探す⇒4
print(numbers.index(3, 5, 9), end=",") #インデックス **5以上9未満（つまり 5, 6, 7, 8）**の範囲で 3 を探す⇒7
#list.index(value, start=0, stop=len(list))



#37
import re

text = "Hello 2020 Python World Pytho"

# \b は単語の境界を表す
print(re.findall(r"\b\w", text)) #\w は単語文字（英数字とアンダースコア）を表す
print(re.findall(r"\b\d.", text)) #\dは数字を表す .は任意の1文字を表す \dで最初の数字2を取り出し、.で次の文字0を取り出す
print(re.findall(r"\bPython?", text)) #?は0回または1回の出現を表す
print(re.findall(r"\bHe..|W.", text)) #..は任意の2文字を表す ||はorを表す

print("--" * 20)
text2 = "ABC abc Good Morning"
print(re.findall(r"[A-Z]", text2)) #大文字のアルファベットを取り出す

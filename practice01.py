li = [5, 1, 2, 3]
print(sorted(li, reverse=True))
#sorted降順に出力

li2 = []
for i in range(10):
    if i % 2 == 0:
        li2.append(i)
#  li2 = [i for i in range(10) if i % 2 ==0]
#内包表記





#1 A 〇
#2 B ⇒D
#3 B 〇

#4 B 〇
x = 42
if x == 0:
    print("xは0")
elif x > 1:
    print("xは1より大きい")
elif x > 10:
    print("xは10より大きい")
elif x < 50:
    print("xは50未満の整数")
# 答え⇒B xは1より大きい

#5 C 〇
a = 10
b = 20
a,b = b,a
print("a:", a, "b:",b)
# C a:20 b:10

#6 A   D
#7 C 〇
#8 A 〇
#9 C 〇
#第１章 7/9


#第２章 テキストと数の操作

#1 D76 ⇒ C76.0  /を使うと浮動小数点数になる
x = 100 - 5**2 + 5 / 5
print(x)

#2 A B
text = (
    "Usage: "
    "-h help"
    "-v version"
)
print(f"第２章２:",text)

text = (
    "Usage: -h help -v version"
)
print(f"第2章2B:",text)

text = (
    "Usage:" "-h help" "-v version"
)
print(f"第2章2C:",text)

#3 B D
text3 = """spam
ham
eggs
"""
print(text3)

#4 D


#5 D A
word = "abcdefg"
slice_word = word[2:5]
print(slice_word)
# D cde

#6 C
word2 = "abcdefg"
slice_word2= word[-5]
print(slice_word2)
#bcdef

#7 B
price = 15000
print(f"価格:{price:7d}")

#8 A
import math
print(f"πの値はおよそ{math.pi:.5f}である")


#9 C
x = 300
y = 150
z = 200
print("spam:{0}, ham:{1}, eggs:{2}" .format(x,y,z))
#print("spam:{x}, ham:{y}, eggs{z}" .format(x,y,z))
print("spam:{}, ham:{}, eggs:{}".format(x,y,z))
print("spam:{a}, ham:{b}, eggs:{c}".format(a=x,b=y,c=z))

#P67 第5章関数
#1 C 〇
#2 D ⇒C
#3 D? ⇒A

#4 B
def function(x, y="foo",z="bar"):
    print(x,y,z)
function("spam",y="ham", z="eggs")

#5 A
default_message_1 = "Hello"

def message(message_1=default_message_1, message_2=""):
    print(f"{message_1} {message_2}")
    
default_message_1 = "こんにちは"
message_2 = "world"

message(message_2=message_2)


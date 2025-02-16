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
#3 B

#4
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

#5
a = 10
b = 20
a,b = b,a
print("a:", a, "b:",b)
# a:20 b:10

#6 A
#7 C
#8 A
#9 C



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


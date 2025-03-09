#第4章 判定と繰り返し

#1 B
for i in range(1,7):
    if i %  2 == 0 and i % 3 == 0:
        print(f"{i}は6の倍数です")
    elif i % 2 == 0 or i % 3 == 0:
        print(f"{i}は2か3の倍数です")
    else:
        print(f"{i}は2の倍数でも3の倍数でもありません")

#2 C A
def num(value):
    return value

value1 = num(0) and num(1) and num(2)
value2 = num(0) or num(1) or num(2)
print(value1, value2)
#and 演算子は最初に偽と評価された値を返し、or 演算子は最初に真と評価された値を返します。
#and 演算子は、最初の False を見つけると、それ以降のオペランドを評価せずに False を返します。
#⇒0
#or 演算子は、少なくとも 1 つのオペランドが True (または True と評価される値) の場合に True を返します。
#⇒1

#3 A C

#4 D

#5 B C
for a in range(4):
    print(a)
for b in range(0, 4):
    print(b)
for c in range(1, 4):
    print(c)
for d in range(1, 8, 2):
    print(d)
#6 A
for c6a in "HELLO":
    if c6a == "L":
        break
    print(f"6A:",c6a)

for c6b in "HELLO":
    if c6b == "L":
        continue
    print(f"6B:",c6b)

#7 C

#8 C
for i, c in enumerate("WORD"):
    if i == 2:
        print(c)
#enumerate()関数は、イテラブルオブジェクト（リスト、タプル、文字列など）の要素とそのインデックスを同時に取得するための便利な組み込み関数です
#例
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
    '''
Index: 0, Fruit: apple
Index: 1, Fruit: banana
Index: 2, Fruit: orange
    '''

#9 C D
print(list(reversed(sorted("EAT"))))
#sorted⇒昇順AETになる
#reversed⇒逆順TEA
#関数がネストしている場合、最も内側の関数から順に実行されます。



#10 B D
for n, c in zip([1, 2, 3], ["1", "2", "3"]):
    print(c * n)
#1*"1" 2*"2" 3*"3"
# 1 22 333になる
#例
for a, b in zip([1, 2, 3], ["5", "6", "7"]):
    print(b * a)#5 66 777
#例２
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 28]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")   
    

# 5/10

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

#3 A C

#4 D

#5 B C

#6 A

#7 C

#8 C

#9 C D
print(list(reversed(sorted("EAT"))))
#sorted⇒昇順AETになる
#reversed⇒逆順TEA

#10 B D
for n, c in zip([1, 2, 3], ["1", "2", "3"]):
    print(c * n)
#1*"1" 2*"2" 3*"3"
# 1 22 333になる
#例
for a, b in zip([1, 2, 3], ["5", "6", "7"]):
    print(b * a)#5 66 777

# 5/10

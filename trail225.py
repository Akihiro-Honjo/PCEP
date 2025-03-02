###3 C
a ="It's OK"
b = '''1.'1. one\n2. two'''
c = 'one' 'two'
# d =  ""Hi!""

print(a)
print(b)
print(c)


###4 C
it = "telescope"
print(it[6:] + it[2:5])
# 6: 位置6（含む）から最後まで ope
#2:5 位置2（含む）から位置5（含まない）まで les

###5 A
name_a = "small"
name_b = "calorie"
name_c = "aluminum"
name_d = "oriental"
print(name_a[-3:-1])#al
print(name_b[-3:-1])#ri
print(name_c[-3:-1])#um
print(name_d[-3:-1])#ta

###6  C
ch1 = "1" 
ch2 = "3" 
print(ch1 * 2 + ch2) #113


###8 C
month, day = 12, 24 
a, b = day + 1, (month + 1) % 12 
print(a, b) #25 1  %はあまり /は整数部分10/3の場合は3

###9 C
types = ["float", "int", "str"] 
for t in types: 
    if len(t) == 3: 
        print(t)
        #int
        #str
'''
1.for t in types: ループが開始され、最初の要素 "float" が t に代入されます。
2.if len(t) == 3: の条件が評価されます。"float" の長さは 5 なので、条件は偽となり、print(t) は実行されません。
3.ループが次の要素 "int" に進みます。
4.if len(t) == 3: の条件が評価されます。"int" の長さは 3 なので、条件は真となり、print(t) が実行されます。
5.print(t) は "int" を出力し、改行します。
6.ループが次の要素 "str" に進みます。
7.if len(t) == 3: の条件が評価されます。"str" の長さは 3 なので、条件は真となり、print(t) が実行されます。
8.print(t) は "str" を出力し、改行します。
9.ループが終了します。
'''        

###10 D
numbers_list = [[1, 3, 5], [1, 2, 3]] 
for numbers in numbers_list: 
    print(numbers, end=" ") 
    for number in numbers:
        if number % 2 ==0:
            print("Even numbers found")
            break
    else:
        print("All numbers are odd")
#テキストP26

###11
def calc(value, x=2): 
    return value ** x 
print(calc(2, 3) * calc(3))#72
'''
def calc(value, x=2):：calcという名前の関数を定義しています。
valueとxは引数（ひきすう）と呼ばれるもので、関数に渡す値を受け取るための変数です。
x=2は、xのデフォルト値（初期値）を2に設定しています。つまり、calc関数を呼び出すときにxの値を省略すると、自動的に2が使われます。
return value ** x：valueのx乗（べき乗）を計算し、その結果を関数の戻り値（返り値）として返します。**はPythonでべき乗を計算するための演算子です。
calc(2, 3)：calc関数を呼び出しています。
valueに2、xに3を渡しています。
calc(2, 3)は2の3乗、つまり8を返します。
calc(3)：もう一度calc関数を呼び出しています。
valueに3を渡していますが、xは省略しています。
xを省略した場合、デフォルト値の2が使われます。
calc(3)は3の2乗、つまり9を返します。
calc(2, 3) * calc(3)：2つのcalc関数の呼び出し結果（8と9）を掛け合わせています。結果は72です。
print(...)：計算結果の72をコンソールに出力します。
'''

###12 B
def greeting(*messages, **options ): 
    for message in messages: 
        print(message, **options) 
greeting("Hello", "Good bye", end="! ")

###13 A
'''
位置専用引数: /より前に定義された引数は、位置引数としてのみ指定可能
キーワード専用引数: *より後に定義された引数は、キーワード引数としてのみ指定可能
'''

###14 C
def greeting(*messages, to=None): 
    pass

###15


###16 c
address = ["hokkaido", "mie", "akita"] 
address.sort(key=lambda s: len(s)) 
print(address)
'''
文字数の少ない順に
'''

###18 C
vegetables = ["tomato"] 
vegetables.append("carrot") 
vegetables.append("potato") #["tomato", "carrot", "potato"]
vegetables.reverse() #["potato","carrot","tomato"]
vegetables.pop() #["potato","carrot"]
vegetables.pop() #["potato"]
print(vegetables)
'''
POP()リストの末尾の要素を削除
'''

###19 B
print([[3 * i + j + 1 for j in range(3)] for i in range(2)])

###20
odds = {3, 5, 7, 9, 11} 
primes = {2, 3, 5, 7, 11}
print(primes - odds, odds | primes)#{2} {2, 3, 5, 7, 9, 11}

'''
^ (排他的論理和): 両方の集合の要素のうち、どちらか一方にのみ含まれる要素の集合を返します。
& (積集合): 両方の集合に共通して含まれる要素の集合を返します。
| (和集合): 両方の集合に含まれるすべての要素の集合を返します。
- (差集合): 左側の集合にのみ含まれ、右側の集合には含まれない要素の集合を返します。
'''
# A. ① primes ^ odds ② odds & primes {2, 9} {3, 5, 7, 11}
print(f"A:" ,primes ^ odds,odds & primes)
#B. ① primes ^ odds ② odds | primes {2, 9} {2, 3, 5, 7, 9, 11}
print(f"B:",primes ^ odds, odds | primes)
#C. ① primes - odds ② odds & primes {2} {3, 5, 7, 11}
print(f"C:",primes - odds, odds & primes)
#D. ① primes - odds ② odds | primes {2} {2, 3, 5, 7, 11}
print(f"D:", primes - odds, odds | primes)


###21 B
'''
A. {"carrot": 80, "tomato": 100}: これは、キーと値のペアを直接指定する、最も一般的なディクショナリの作成方法です。
B. dict("carrot"=80, "tomato"=100): dict() コンストラクタでキーワード引数を使用する場合、キーワードは文字列ではなく、Pythonの識別子として扱われます。したがって、"carrot" のように引用符で囲むことはできません。正しい構文は dict(carrot=80, tomato=100) です。
C. dict([("carrot", 80), ("tomato", 100)]): dict() コンストラクタに、キーと値のペアのタプルを含むリストを渡す方法です。
D. {k: v for k, v in [("carrot", 80), ("tomato", 100)]}: これは、辞書内包表記を使用してディクショナリを作成する方法です。リスト内の各タプルからキーと値を取り出し、新しいディクショナリを作成します。
'''

###22 C
vegetables = {0: "carrot", 1: "potato", 2: "tomato"} 
for kv in  vegetables.items():
    print(kv)
#(0, 'carrot') 
#(1, 'potato') 
#(2, 'tomato')

###23 B
temp = 22 
print( temp >= 10 or temp < 20)#True


###24 B
compare1 = "carrot" < "tomato" < "potato"
compare2 = [3, 2] < [3, 1, 4] 
compare3 = (3, 1) < (3, 1, -1) 
print(compare1, compare2, compare3)
#False False True
'''
①文字列は辞書順
compare1 = "carrot" < "tomato" < "potato"はFalse
②リストの比較
compare2 = [3, 2] < [3, 1, 4] 0番目の3は同じ、1番目の2と1で比較
False
③タ
プルの比較 要素数がことなる場合、要素数の少ないほうが、小さいと評価されます。
compare3 = (3, 1) < (3, 1, -1) はTrue
'''

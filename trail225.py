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
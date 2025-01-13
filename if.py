#if文
#比較演算子
english = 80
math = 90
total = english + math
standard = 150

if total >= standard:
    print("合格")
else:
    print("不合格")

#論理演算子
is_foods = True
take_out = True

if is_foods and take_out:
    print("8％")
else:
    print("10％")

#数値、文字列、リスト、Noneの真偽値
string = ''

if string:
    print(f"string is {string}")
else:
    print("string is empty")

#if文の中にif文（七五三）

age = 7
gender = 'female'

if gender == 'female':
    if age == 7:
        print('7才の女の子です')
    elif age == 3:
        print('3才の女の子です')
    elif age == 'male' and age == 5:
        print('5才の男の子です')
    else:
        print('該当なし')
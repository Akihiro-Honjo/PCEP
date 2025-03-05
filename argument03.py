#位置引数とキーワード引数の組み合わせ
def bill(unit_price, quantity, has_app): #単価、個数、アプリ有無
    amount =unit_price * quantity
    point = amount * 0.01 if has_app else 0 #Trueの時 if elseのとき
    return unit_price * quantity,point

my_amount, my_point = bill(100, 10, True)
print(my_amount, my_point)

#位置引数を先に渡す NG例:my_amount, my_point = bill(unit_price=100, 10, True)
#キーワード引数の後に位置引数を定義できない


###型アノテーション(期待する型を明示)
def greet(name:str, age:int, height:float) -> str:
    return f'hello,{name}. You are {age} years old and {height}cm tall'

name: str = 'Taro'
age: int = 20
height: float = 170.0

print(greet(name, age, height))

###可変長引数
# *args 任意の数の位置引数を受け取る 引数名の前に*をつける
# *argsの後ろはキーワード引数で指定する
def sum_func(multi, *args, div=100):
    print(*args)
    print(multi, div)
    return sum(args)

total = sum_func(10,1,2,3,4,5, div=10)
print(total)
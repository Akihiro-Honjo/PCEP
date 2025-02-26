#位置引数とキーワード引数の組み合わせ
def bill(unit_price, quantity, has_app): #単価、個数、アプリ有無
    amount =unit_price * quantity
    point = amount * 0.01 if has_app else 0 #Trueの時 if elseのとき
    return unit_price * quantity,point

my_amount, my_point = bill(100, 10, True)
print(my_amount, my_point)

#位置引数を先に渡す NG例:my_amount, my_point = bill(unit_price=100, 10, True)
#キーワード引数の後に位置引数を定義できない
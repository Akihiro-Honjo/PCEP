#関数へ変数に代入する
def add(x, y):
    return x + y
add_variable = add
result = add_variable(1, 2)
print(add_variable) 
print(result)

def add2(*args, func):
    return func(*args)

add_variable2 = add2
result = add_variable2([1, 2, 3, 4, 5], func=sum)
print(result)


def subtract(x, y):
    return x - y
def division(x, y):
    return x / y
def multiply(x, y):
    return x * y
def calculate(func, x, y):
    return func(x, y)

result = calculate(multiply, 10, 20)
print(result)
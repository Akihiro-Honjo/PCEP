#関数 def⇒define定義
def greet(name):
    print(f"Hello {name}!")
    print("This is a basic python program")

greet("Taro")
greet("Yamada")

my_greet = greet
my_greet("John")

def add_number(x, y):
    return x + y

add_num = add_number(5, 10)
print(add_num)


def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a ,b):
    return a * b 
def division(a, b):
    return a / b
def calculate(func, a, b):
    return func(a, b)

def return_calc(calc_name):
    if calc_name == "add":
        return add
    elif calc_name == "subtract":
        return subtract
    elif calc_name == "multiply":
        return multiply
    elif calc_name == "division":
        return division
    

#add_n =add
result = calculate(return_calc("add"), 10, 20)
print(result)


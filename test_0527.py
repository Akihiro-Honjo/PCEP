for i in range(-3, -13, -3):
    print(i, end=",")
    
print('-'*30)

fruits = ['apple', 'orange']
drinks = ['water', 'coffee']
for fruit in fruits:
    for drink in drinks:
        print(fruit, drink)
        
print('-'*30)

def function(a, list=[]):
    list.append(a)
    print(list)
function(1)
function(2)
function(3)

print('-'*30)

colors = ['red', 'blue', 'black', 'red', 'green', 'white', 'red', 'yellow']
colors.count('red')
print(colors.count('red'))  # Count occurrences of 'red'

print('-'*30)

numbers = []
for x in range(5):
  numbers.append(x ** 2)

numbers = [x ** 2 for x in range(5)]
#[式 for 変数名 in イテラブルオブジェクト]
print(numbers)  # List comprehension to create a list of squares

print('-'*30)

colors = ["red", "black", "green", "blue"]
for color in colors[:]:
    if len(color) > 4:
        colors.pop()
        colors.insert(0, color)
print(colors)


d = {x: x*2 -1 for x in [1, 2, 3]}
print(d)

a = [1, 3, 5, 7, 9]
if 2 not in a:
    print("リストaに2はありません")
if 10 > 5 and not 5 > 7:
    print("Trueです")
else:
    print("Falseです")

class TestError(Exception): 
    pass 

def test1(): 
    try: 
        test2()
    except TestError: 
        print('php')
    
def test2(): 
    print('python') 
    raise TestError
    print('ruby') 

test1()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

x = [1, 2, 3]
y = x
y.append(4)
print(x)


print('-'*20)
num_lists = [1,2,3,0,1,2,4,5,6]
print(num_lists.index(2,4))


x = 0
while x < 3:
    x += 1
    if x == 2:
        continue
    print(x)


def process_list(data):
    try:
        result = [10 / x for x in data]
        return result
    except ZeroDivisionError:
        return "ゼロで除算が発生しました"
    except TypeError:
        return "要素の型が不正です"

print(process_list([2, 5, 1, 0]))

print('--'*20)

def greet(message="Hello", name):
    print(f"{message}, {name}!")

# greet("Hi", "Alice")
greet("Bob")

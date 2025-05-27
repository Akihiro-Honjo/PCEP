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

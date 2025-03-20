###ラムダ式
#lambda 引数1, 引数2, ... : 式（処理）

##引数に1を足す
#通常の関数
'''
def add_one(x):
    return x + 1
'''
#ラムダ式
add_one = lambda x: x + 1
print(add_one(1))


##2つのうち小さい数値を返す
#通常の関数
'''
def smaller(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
'''

smaller = lambda num1, num2: num1 if num1 < num2 else num2
print(smaller(1, 2))


###ドル円変換
#通常の関数
'''
def usdjpy(dollar, rate):
    return dollar * rate

print(usdjpy(100, 136.28))
'''
usdjpy = lambda dollar, rate: dollar * rate
print(usdjpy(100, 136.28))


###*argsの平均
'''
def average(*args):
    return sum(args) / len(args)
'''
average = lambda *args: sum(args) / len(args)

print(average(1, 2, 3, 4, 5))


def by_last_letter(word):
    return word[-1]
words = ['apple', 'banana', 'cherry', 'fig', 'grape']
sorted_words = sorted(words, key=lambda word: word[-1])
print(sorted_words)



'''def student_age(student: dict) -> int:
    return student['age']
students: [dict] = [
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 18},
    {'name': 'Charlie', 'age': 19}
]

sorted_students = sorted(students, key=student_age)
print(sorted_students)'''

student_age = lambda student: student['age']
students: [dict] = [
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 18},
    {'name': 'Charlie', 'age': 19}
]
sorted_students = sorted(students, key=student_age)
print(sorted_students)
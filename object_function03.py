###map関数
#与えられた関数をイテラブルのすべての要素に適用し、結果を返す

def square(x):
    return x * x

def add_10(x):
    return x + 10

numbers = [1, 2, 3, 4, 5]
#squares = map(square, numbers)
squares = map(add_10, numbers)

for number in squares:
    print(number)
    
#小文字を大文字に変換
def to_upper(s):
    return s.upper()

langs = ['python', 'java', 'ruby', 'php']
uppers = map(to_upper, langs)
print(list(uppers))

#メートルを尺に変換する 
def to_shaku(meter):
    return meter * 0.3

meters = [1, 2, 3, 4, 5]
shakus = map(to_shaku, meters)
for meter, shaku in zip(meters, shakus):
    print(f'{meter}m = {shaku}shaku')


###filter関数
#与えられたイテラブルから特定の条件を満たす（True）要素のみを抽出するための関数

#偶数のみを抽出する
def is_even(x):
    return x % 2 == 0

numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
even_numbers = filter(is_even, numbers)
#print(list(even_numbers))

for number in even_numbers:
    print(list(even_numbers))

#正の数のみ    
def is_positive(x):
    return x > 0
numbers2 = [-1, 3, -5, 7, 9, -11, 13]

positive_numbers = filter(is_positive, numbers2)
print(list(positive_numbers))

#リスト内のうち特定の文字で始まるものだけを抽出する
def start_with_A(word):
    return word.startswith('A')

words = ['Apple', 'Banana', 'Airplane', 'Car', 'Axe']

for word in filter(start_with_A, words):
    print(word)
    

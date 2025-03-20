def by_length(word):
    return len(word)

fruits = ['apple', 'banana', 'cherry', 'fig', 'grape']
fruits.sort(key=by_length)#短い順
#fruits.sort(key=by_length, reverse=True)#長い順
print(fruits)


#リスト内の数値の絶対値を基準にソート

def by_absolute_value(num):
    return abs(num)

numbers = [-9, -5, -4, 1, 2, 3, 6, 7, 8]
numbers.sort(key=by_absolute_value)
print(numbers)


#文字列の最後の文字を基準のソート
def by_last_letter(word):
    return word[-1]
words = ['apple', 'banana', 'cherry', 'fig', 'grape']
words.sort(key=by_last_letter)
print(words)

#並べ替えたくない場合
def by_last_letter(word):
    return word[-1]
words = ['apple', 'banana', 'cherry', 'fig', 'grape']
sorted_words = sorted(words, key=by_last_letter)
print(sorted_words)
print(words)




def count_up_to(max_number):
    count = 0
    while count <  max_number:
        print(count)
        yield count
        count += 1   
my_gen = count_up_to(7)
print(list(my_gen))
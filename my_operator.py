#累算演算子
'''
a = 10
for _ in range(10):
    a += 1
    print(a)
'''

    

'''
x = x +1 #x += 1と同じ
x = x % 2 #x %= 2と同じ
'''

#比較演算子
a = 'A'
b = 'B'
print('a' == 'a')
print('a' == 'b')

foo ='foo'
bar = 'bar'
print(foo is bar)
spam = 'foo'
print(id(foo), id(bar), id(spam))
print(foo is spam)

print('th' in 'python') #True
print('Py' in 'python') #False
print(3 in [1, 2, 3]) #True


#比較の連鎖

def test(val):
 print('test')
 return val


x = 18
print(10 < test(x) < 20) #True
print(10 < test(x) and test(x) < 20) #True


x = 18
print(10 < x < 20) #True
print(10 < x and x < 20) #True


y = 8
print(10 < x < 20 < y) #False
print(10 < x and x < 20 and 20 < y) #False

print(len('abc'))
print(test('abc'))

year = 1998
if year < 1868:
    print('江戸時代以前')
elif 1868<= year < 1912:
    print('明治時代')
elif 1912<= year < 1926:
    print('大正時代')
elif 1926<= year < 1989:
    print('昭和時代')
elif 1989<= year < 2019:
    print('平成時代')
else:
    print('令和時代')
    

#論理演算子
is_like_baseball = True
is_like_soccer = True
is_like_tennis = False
result = is_like_baseball and is_like_soccer
print(result)#True

result2 = is_like_baseball or is_like_tennis
print(result2)#True

result3 = is_like_baseball and is_like_tennis
print(result3)#False


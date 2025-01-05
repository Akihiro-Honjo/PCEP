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

Zen = 'SimpleIsBetterThanComplex'


print(Zen[:])
print(Zen[1000:])
print(Zen[5:1000])


print('-' * 30)

i = 5
i = 6
# i = 10

def f(arg = i):
    i = 7
    print(arg)

i = 8
i = 9

f()

print('-' * 30)

list = [-10, 1, 15, 20, 30]
list.insert(2, 5)
list.append(50)
list.sort(reverse=True)
list.pop(-1)
print(list)

print('-' * 30)


a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a+b


print('\n' + '-' * 30)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        print(n, 'is a prime number')
        
print('-' * 30)


Zen = ['Now','is','better','than','never']
for i ,v in enumerate(Zen):
    print(i, v)
print('-' * 30)
Zen = ['Now','is','better','than','never']
for i in range(len(Zen)):
    print(i, Zen[i])


print('-' * 30)

s = "abc"
s = s.replace('a', 'A')
print(s)




print('-' * 30)


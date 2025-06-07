print("Python"[::-1])

import math
print(math.ceil(4.2))

a = [1, 2, 3]
a.append([4, 5])
print(a)
a.extend([6, 7])
print(a)


print('-' *30)


x = [1, 2, 3]
y = x[:]
x[0] = 100
print(y)
print(x)

swimmer = [s * 2 for s in 'swimmer']
print(swimmer)
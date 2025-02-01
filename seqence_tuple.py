t = ("Bob" , "Tom", "Ken")
print(t[0])
print(t)


l = [1, 2, 3, 4, 5, 6]
l = tuple(l)
print(l)


#タプルメモリ使用量
import sys

LENGTH = 999999
my_list = list(range(LENGTH))
my_tuple = tuple(range(LENGTH))
print(f'list:{sys.getsizeof(my_list)}')
print(f'tuple:{sys.getsizeof(my_tuple)}')

def foo(num):
    return num +1, num ** 2

f, f2 = foo(10)
print(f, f2)
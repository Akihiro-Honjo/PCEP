numbers = list(range(1, 11))

# 偶数要素だけを二乗
squared_even_numbers = [x**2 for x in numbers if x % 2 ==0 ]

print(squared_even_numbers)

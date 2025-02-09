numbers = list(range(1, 20))

# 奇数要素だけを二乗
#squared_odd_numbers_dict = {num:(""if num % 2 ==0 else num**2)for num in numbers}
squared_odd_numbers_dict = {num: num**2 for num in numbers if num % 2 == 1}
print(squared_odd_numbers_dict)
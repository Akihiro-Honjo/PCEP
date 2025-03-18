def sum_numbers(*args):
    total = 0 #ローカル関数
    for number in args:
        total += number
    print(total)

total = 999 #グローバル関数
sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) #55
print(total)
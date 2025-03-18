def sum_numbers(*args):
    global total
    total = 0
    for number in args:
        total += number
    print(total, id(total))

total = 999
sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) #55
print(total, id(total))
#同じidになる
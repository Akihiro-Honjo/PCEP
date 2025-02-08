#else
num  = 0
while num < 5:
    print(num)
    num += 1
else:
    print("else:", num)
    
    
#continue
num2 = 0
while num2 < 30:
    if num2 % 2 == 0:
        num2 += 1
        continue
    print(num2) 
    num2 += 1
else:
    print("else:", num2)
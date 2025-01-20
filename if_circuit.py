def return_true():
    return True

#print(return_true()) # True

a = False

if a and return_true():
    print("True")
else:
    print("False")
    
'''
#三項演算子

#通常のif文
if x > 0:
    y = "positive"
else:
    'y = "Non-positive"'
#三項演算子
y = "positive" if x > 0 else "Non-positive"

'''

age = 18
is_adult = True if age >= 18 else False
print(is_adult) # True
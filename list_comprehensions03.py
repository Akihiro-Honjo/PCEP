#all()すべて条件を満たすか any()複数のうちどれかが条件を満たす
list1 = [True, True, True]
list2 = [False, False, True]
list3 = [False, False, False]

print(all(list1))
print(all(list2))
print(all(list3))

print(any(list1))
print(any(list2))
print(any(list3))


kokugo = 80
english = 70
math = 85
# if kokugo >= 80 and english >= 80 and math >= 80:
#     print("合格")
# else:
#     print("不合格")
result = all([kokugo >= 80, english >= 80, math >= 80])
if result:
    print("合格")
else:
    print("不合格")

def judge(subject):
    return subject >=80
result = all([judge(kokugo), judge(english), judge(math)])
if result:
    print("合格")
else:
    print("不合格")
    

subjects = {
    "kokugo":80,
    "english":80,
    "math":85,
    "science":90,
    "society":90,
}
result2 = all(subject >=80 for subject in subjects.values())
if result2:
    print("合格")
else:
    print("不合格")
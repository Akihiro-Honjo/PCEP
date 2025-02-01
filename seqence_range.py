rng = range(10)
print(list(rng))
for _ in rng:
    print(_)
    
rng2 = range(10, 30, 2)

for _ in rng2:
    print(_)
    

#合計を得る
rng3 = range(100)
print(sum(rng3))


#
names = ['Alice', 'Bob', 'Charlie']

for name in names:
    print(name)
# for i in range(len(names)):
#     print(i, names[i])
for i, name in enumerate(names):#enumerate関数
    print(i, name)
    
#str型
s = 'abcdefg'
print(s[0])
print(s[5])

for _ in s:
    print(_)
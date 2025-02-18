#第3章 リストの操作 P38


#1 B C

#2 D B
data = [1, 2, 3, 4]
print(data[:2], data[3:])
#[1, 2, 3] [4]  ⇒  [1, 2][4]

#3 C 〇
data2 = [1, 2]
data2.append(3)
print(data2)#[1, 2, 3] 

#4 B 〇

#5 B? 〇 [[1, 2, 3, 4]] この長さは1

#6 A 〇
data3 = [1, 2],[3, 4]
print(data3[0][0], data3[1][1])#[1, 4]

#7 C A
stack = [1, 2, 3, 4]
data4 = []
while stack:
    #data4.append(stack.pop(0))
    data4.append(stack.pop())
print(data4)

#8 B 〇
data8 = [1, 2]
data8.append(3)
data.pop(0)
print(data8)#[2, 3]

#9 A 〇
data9 = []
for i in [1, 2, 3]:
    for j in [1, 2]:
        if i != j:
            data.append((i, j))
print(data9)

#6/9正解


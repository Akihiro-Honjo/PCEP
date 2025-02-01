#データ構造set型
#集合演算を効率的に実行するために多く使用する


set_1 = {1, 1, 1, 2, 2, 2, 3, 3, 3}
print(set_1)
print(type(set_1))

list_1 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
set_2 = set(list_1)
print(set_2)

#要素の追加、削除、存在確認
set_3 = {1, 1, 1, 2, 2, 2, 3, 3, 3}
set_3.add(4)#追加
set_3.remove(3)#削除
result = 1 in set_3 #存在確認
print(set_3)
print(result)#True



#集合演算
A = {"yamada", "sato", "suzuki"}
B = {"yamada", "suzuki", "takahashi"}

print(A | B) #和集合 print(A.union(B))
print(A & B) #積集合 print(A.intersection(B))
print(A - B) #差集合 print(A.difference(B)) Aだけに所属している人
print(A ^ B) #対称差集合 print(A.symmetric_difference(B)) どちらかにしか所属していない

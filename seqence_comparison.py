#シーケンスの大小比較
lst = [1, 2, 3]
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [1, 2, 4]
print(lst1 == lst2)
print(lst == lst1)
print(lst1 < lst3) #最初の異なる要素で比較

#異なる型の比較(大小比較は同じ型に変換する)
l1 = [1, 2, 3]
l2 = (1, 2, 3) 
print(l1 == l2)#False
print(l1 == list(l2))#True
print(l1 < list(l2))#False

#中に違う型が入っていても比較できる（構成が同じの場合）
a1 = [1, 'Apple' ,3.14]
a2 = [1, 'Apple' ,3.14]
print(a1 == a2)
print(a1 < a2)
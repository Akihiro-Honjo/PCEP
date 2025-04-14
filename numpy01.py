import numpy as np

#一次元配列を作成
arr1 = np.array([1, 2, 3, 4, 5])
print("一次元配列", arr1)
print(arr1[0]) # 1番目の要素を取得

#二次元配列
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("二次元配列", arr2)

#配列の形状を取得
print("arr1の形状", arr1.shape) # (5,)
print("arr2の形状", arr2.shape) # (2, 3)

#配列の要素の合計
print("arr1の合計", arr1.sum()) # 15
print("arr2の合計", arr2.sum()) # 21

#配列の要素の平均
print("arr1の平均", arr1.mean()) # 3.0  
print("arr2の平均", arr2.mean()) # 3.5

#配列の要素に対するsinを計算
print("arr1のsin", np.sin(arr1)) # [0.84147098 0.90929743 0.14112001 -0.7568025 -0.95892427]
print("arr2のsin", np.sin(arr2)) # [[0.84147098 0.90929743 0.14112001] [-0.7568025 -0.95892427 -0.2794155 ]]
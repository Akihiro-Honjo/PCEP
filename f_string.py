#f文字列 r文字列
first_name = "Taro"
last_name = "Yamada"

print(f'Hello {first_name} {last_name}')

print("C:\\path\\to\\file")
print(r"C:\path\to\file")


#関数とメソッド
#len()関数
print(len('python'))#6
x = ['python', 'java', 'ruby']#要素数
print(len(x))#3

#strip()メソッド,replase()メソッド
print('python'.strip('thon'))#py
s = 'python'
print(s.replace('py' , 'zz')) #zzthon

#zfill()メソッド ゼロ埋め
num = 10
print(str(num).zfill(5)) #00010

#find()メソッド, index()メソッド
#0から始まるインデックスを返す
#find()メソッドは見つからない場合-1を返す
#index()メソッドは見つからない場合ValueErrorを返す
y = 'python python'
print(y.find('p')) #0
print(y.index('p')) #0
print(y.find('o', 7)) #11
print(y.find('T'))#-1
# print(y.index('T'))#ValueError

#in演算子 大文字小文字を区別する
a = 'Taro Yamada'
print('Taro' in a) #True
print('taro' in a) #False
print('T' and 'Y' in a) #True
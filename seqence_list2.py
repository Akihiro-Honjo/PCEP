#remove()メソッド
fruits = ['apple', 'banana', 'orange']
banana = fruits[1]
fruits.remove(banana)
print(fruits)

fruits = ['apple', 'banana', 'orange' , 'banana']
banana = fruits[1]
fruits.remove(banana)
print(fruits)



fruits2 = ['apple2', 'banana2', 'orange2' , 'banana2']
banana2 = fruits2[1]

del fruits2[1]
'''
if 'banana2' in fruits2:
    fruits2.remove('banana2')
'''
print(fruits2)

fruits3 = ['apple3', 'banana3', 'orange3' , 'banana3']
fruits3.clear()
print(fruits3)


#index() リスト内の位置がわかる
fruits4 = ['apple4', 'banana4', 'orange4' , 'banana4']
orange_index = fruits4.index('orange4')
print(orange_index)

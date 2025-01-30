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

#countメソッド
banana4_count =  fruits4.count('banana4')
print(banana4_count)#2
banana4_count =  fruits4.count('Banana4')
print(banana4_count)#0

#reverseメソッド（順番を逆転）
reversed_fruits = fruits4.copy()
reversed_fruits.reverse()
print(fruits4)
print(reversed_fruits)


name = ["Alice", "Bob", "Charlie", "Dave"]
name.sort()
print(name)

name2 = ["Alice", "Bob", "Charlie", "Dave"]
name2.sort(reverse=True)
print(name2)

#浅いコピー
copy_name = name.copy()
name[0] = 'taro'
print(name)
print(copy_name)

#深いコピー
import copy

name3 = [
    ["太郎", "花子"],
    ["健太", "結衣"],
    ["イチロー"]
]
copy_name3 = copy.deepcopy(name3)
print(copy_name3)


nums = list(range(11))
print(nums)
print(max(nums))
print(min(nums))
print(sum(nums))

strs = ["a", "b", "c", "d", "e"]
print(max(strs))
print(min(strs))

strs1 = "b" in strs
if strs1:
    print('b is in strs')
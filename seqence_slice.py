#n番目からm番目までの要素を取り出す
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[3:8])# [4, 5, 6, 7]
#:の右側は1から数える。この場合だと[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[-7:-2])
#:の右側（負）の場合[-9, -8, -7, -6, -5, -4, -3, -2, -1]9はない
print(my_list[-7:])
print(my_list[:3])
names = ['John', 'Paul', 'George', 'Ringo']

#nステップ（n個間隔）
my_list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list2[::2])# [0, 2, 4, 6, 8]
print(my_list2[2:9:3])# [2, 5, 8]
print(my_list2[::-1])# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

m = my_list2[5::2]
print(m)
print(m[1])

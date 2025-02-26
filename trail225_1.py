it = "telescope"
print(it[:2])#te 2を含まない #0 t 1 e :2 l 3 e 4 s 5 c 6 o 7 p 8 e 9
print(it[2:])#lescope 2を含む後ろ #0 t 1 e 2: l 3 e 4 s 5 c 6 o 7 p 8 e 9
print(it[:9])#telescope
#0 t 1 e 2 l 3 e 4 s 5 c 6 o 7 p 8 e 9

print(it[6:] + it[2:5])
#0 t 1 e 2 l 3 e 4 s 5 c 6: o 7 p 8 e 9 ⇒ ope
#0 t 1 e 2: l 3 e 4 s :5 c 6 o 7 p 8 e 9 ⇒les
#答えはopeles

name_a = "small"#-5 s -4 m -3: a -2 l :-1 l
name_b = "calorie" #-7 c -6 a -5 l -4 o -3: r -2 i :-1 e ⇒ ri
name_c = "aluminum"
name_d = "oriental"
print(name_a[-3:-1])
print(name_b[-3:-1])


'''

:4 後ろは含まない
2: 前は含む

'''
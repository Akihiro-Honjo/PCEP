rate = 0.7
if rate >= 0.8:
    print('カッパを持って行ってください')
elif rate >= 0.4:
    print('傘を持って行ってください')
elif rate >= 0.6:
    print('折り畳み傘を持って行ってください')
else:
    print('傘はいりません')
#条件分岐は上から適用される

# rate = 0.8
# if rate >= 0.8:
#     print('カッパを持って行ってください')
# elif rate >= 0.6:
#     print('傘を持って行ってください')
# elif rate >= 0.4:
#     print('折り畳み傘を持って行ってください')
# else:
#     print('傘はいりません')

a = 10
b = 5

if a > b:
    print('aはbより大きい')
    if a > 15:
        print('aは15より大きい')
    elif a > 12:
        print('aは12より大きい')
    else:
        print('aは12以下')
else:#この場合だと下記は実行されない
    print('aはbより小さい')
    if b < 0:
        print('bは負の値です')
    else:
        print('bは正の値です')
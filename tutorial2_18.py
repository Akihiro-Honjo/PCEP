text = '彼は「それは\'本当\'です」と言った。'
print(text)#彼は「それは'本当'です」と言った。

text2 = 3 * 'un' + 'ium'
print(text2)#unununinm
#unを3回繰り返す

x = 100 - 5**2 + 5 / 5
print(x)#76.0 /を使うと浮動小数点数になる

x2 = 100 - 5**2+ 1
print(x2) #76

text3 = (
    "Usage: "
    "-h help"
    "-v version"
)
print(text3) #Usage: -h help-v version

text4 = """spam
ham
eggs
"""
print(text4)
#spam
#ham
#eggs
# """改行


word = "abcdefg"
slice_word = word[2:5]
print(slice_word) #cde
#文字列abcdefgの場合に考え方
#0 a 1 b 2 c 3 d 4 e 5 f 6 g 7
#2～5までなのでcdeとなる
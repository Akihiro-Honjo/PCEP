#10
text = "Hello, python"
for t in text:
    if t == "p":
        break
    print(t)
    
#12
num = 1

def add(a, b=10):
    num = 5
    print(a + b)

num = 2
add(num)

#13
def test(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
test("Yamada", "特技は水泳", "趣味は読書",  job="デザイナー", age=18)

#14
list =  ["特技は水泳", "趣味は読書"]
print(*list)


#15
fun = lambda a, b: a + b
print(fun(5, 2))

names = ['Tanaka', 'Sato', 'Yamada']
names.sort(key=lambda x: len(x))
print(names)
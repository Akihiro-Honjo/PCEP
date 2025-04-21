import sys

print(type(sys.argv))
print("スクリプト名", sys.argv[0])
#print("引数", sys.argv[1])
for i, arg in enumerate(sys.argv):
    print(i, "番目の引数", arg, type(arg))
    
    

def multiply(x, y):
    return x * y

print(multiply(int(sys.argv[1]), int(sys.argv[2])))
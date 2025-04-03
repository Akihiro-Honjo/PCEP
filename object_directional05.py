###名前空間
#LEGBルール
# 1.Local
# 2.Enclosing
# 3.Global
# 4.Built-in

import builtins
from pprint import pprint

#グローバル変数
x = 1

def outer():
    #エンクロージング変数
    x = 2
    
    def inner():
        #ローカル変数
        x = 3
        print('outer', x)
        print('locals', locals())
        pprint(globals())
    
    print('inner', x)
    inner()

def print(*args, **kwargs):
    builtins.print('my print', *args, **kwargs)
    
outer()
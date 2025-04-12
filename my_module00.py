#my_module.pyよりインポートする
import my_module
from my_module import subtract

import my_module as mm

#並び順
#標準ライブラリ⇒サードパーティライブラリ⇒自作モジュール（1行あけて）
#複数行のインポートは①（）を使う、②\を使う、③importを複数行書く

add_result = my_module.add(1, 10)
multiply_result = my_module.multiply(2, 5)

subtract_result = subtract(10, 1)
#fromの場合はmy_module.は不要

divide_result = mm.divide(16, 2)
# asの場合はmy_module.は不要

print(add_result)  # 11
print(multiply_result)  # 10
print(subtract_result)  # 9
print(divide_result)  # 8.0
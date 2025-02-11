def is_palindrome(s):
    # 引数 s が回文かどうか判定して True もしくは False を返す関数を定義してください
    return s == s[::-1]

print(is_palindrome("level"))  # True
print(is_palindrome("radar"))  # True
print(is_palindrome("Python")) # False
print(is_palindrome("たけやぶやけた")) # True
print(is_palindrome("しんぶんし"))     # True
print(is_palindrome("ぱいそん"))       # False


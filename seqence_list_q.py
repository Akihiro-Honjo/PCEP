#スタック（後入れ先出し）
langs = []
langs.append('C')
langs.append('C++')
langs.append('Java')

print(langs.pop())
print(langs.pop())
print(langs.pop())

print(langs)


#キュー（先入れ先だし）
from collections  import deque

r = []
r.append("sato")
r.append("tanaka")
r.append("suzuki")
r.append("sudo")

r2 = deque(r)
print(r2.popleft())
print(r2.popleft())
print(r2.popleft())
print(r2.popleft())
print(r2)
print(r)




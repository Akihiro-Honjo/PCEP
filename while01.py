num = 0
while num  < 5:
    print(num, num < 5)
    num += 1
    

import random
money = int(input("金額を入力してください"))
price = 100
while money >=price:
    money  -= price
    result = random.choice(["レア", "ノーマル", "スーパーレア"])
    print(result,f"残り金額は{money}円です。")
    

def square(x=12, y=2):
    """べき乗する関数""" #docstring
    if x > 10:
        print('xは10以下にしてください')
        return None
    return x**y

result = square()
print(result)
#print(help(square))

import random

def vending_machine(coin): #coinは仮引数:parameter
    """自動販売機関数"""
    if coin < 120:
        return "コインが足りません",coin
    
    lottery_result = random.randint(1,10)
    lottery = ''
    if lottery_result == 10:
        lottery = "あたり"
    else:
        lottery = "はずれ"
    
    return "飲み物", coin-120, lottery 

drink, change, lottery = vending_machine(150) #ここの150は実引数:argument
print(drink, change, lottery)
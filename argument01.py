import random

def vending_machine(coin, drink, application): #coinは仮引数:parameter drink,applicationは下記の"コーラ",Trueと位置引数
    """自動販売機関数"""
    if coin < 120:
        return "コインが足りません",coin
    
    lottery_result = random.randint(1,10)
    lottery = ''
    if lottery_result == 10:
        lottery = "あたり"
    else:
        lottery = "はずれ"
    if application:
        print("ポイントが加算されました")
    
    return drink, coin-120, lottery 

drink, change, lottery = vending_machine(150, "コーラ", True) #ここの150は実引数:argument
#キーワード引数：drink, change, lottery = vending_machine(coin=150, drink="コーラ", application=True) 順番は前後して大丈夫
print(drink, change, lottery)
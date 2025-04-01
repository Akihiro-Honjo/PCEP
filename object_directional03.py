
###継承
class Human: #親クラス
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"こんにちは{self.name}です。年齢は{self.age}歳です。")

class Customer(Human): #子クラス
    def __init__(self, name, age, address):
        super().__init__(name,age) #親クラスから呼び出す
        self.address = address
        
taro = Customer(name="taro", age=34, address="Fukuoka")
taro.greeting()
print(dir(taro))
    
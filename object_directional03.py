
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
    
    def greeting(self):
        print(f"こんにちは{self.name}です。年齢は{self.age}歳です。住所は{self.address}です。")
        #オーバーライド（上書き）
    
    def __str__(self):
        print(f"私の名前は{self.name}")
        
        
taro = Customer(name="taro", age=34, address="Fukuoka")
taro.greeting()
# print(dir(taro))
print(taro.__str__())

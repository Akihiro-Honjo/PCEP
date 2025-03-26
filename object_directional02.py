###隠蔽（カプセル化）
##文法
## 1._メソッド名  
## 2. __メソッド名(アンダーバー2つ(ダンダー)あまり使わない)
## 3.デコレータ@propertyおよび@インスタンス名.setter


##スポーツ事務の顧客クラスの例
class Customer:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    @property
    def age(self):
        return self._age #getter内では _ をつける
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("年齢は整数を入力してください。")
        elif value < 18:
            raise ValueError("未成年は登録できません。")
        self._age = value #setter内では _ をつける
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("身長は数値を入力してください。")
        elif value < 0:
            raise ValueError("身長は正の値を入力してください。")
        self._height = value
    
    @property
    def weight(self):
        return self._weight
    
    def weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("体重は数値を入力してください。")
        elif value < 0:
            raise ValueError("体重は正の値を入力してください。")
        self.weight = value

yamada = Customer(name="Yamada Taro", age=30, height=174.5, weight=60)
print(yamada.age, yamada.height, yamada.weight)
#print(dir(yamada))


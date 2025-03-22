###プライベート変数
## _変数名

class Human:
    species = "ホモサピエンス" #クラス変数
    population = "80億人" #クラス変数
    
    def __init__(self, name, age, gender="unknown"):
        self.name = name
        self._age = age
        self.gender = gender
        self.species = "ホモサピエンス init" #クラスとインスタンスに同名の変数がある場合はインスタンスが優先される。
        
    def say_hello(self):
        print(self._return_hello())    
    def _return_hello(self):
        return f'こんにちは。私は{self.name}です。\n年齢は{self._age}です。\n性別は{self.gender}です。'
    
    @classmethod
    def show_population(cls):
        print(f'現在の人口は{cls.population}です。')



def say_bye():
    print('さようなら。')


#インスタンス       
yamada = Human(name='Taro Yamada', age=20, gender="Male")
yamada.say_hello()
print(yamada.name, yamada.gender)
print(yamada.species, yamada.population)
print(Human.species, Human.population)
print("-" * 50)
yamada.show_population()
Human.show_population()
print("-" * 50)

sato = Human(name='Hanako Sato', age=25, gender="Female")
sato.say_hello()
print(sato.species, sato.population)
sato.species = "ホモサピエンス sato"
print(sato.species, sato.population)

print("-" * 50)
#クラス変数、インスタンス変数整理
print(Human.species, Human.population)
Human.show_population() #クラスメソッド

print("-" * 50)
Human.say_hello(yamada)




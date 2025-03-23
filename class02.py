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

#hasattr
print("*" * 50)
print('name',hasattr(yamada, 'name')) #True
print('say_hello', hasattr(yamada, 'say_hello')) #True

#getattr オブジェクトの属性を取得する
print("*" * 50)
yamada_name = getattr(yamada, 'name')
yamada_hello = getattr(yamada, 'say_hello')
print(yamada_name)
yamada_hello()


#setattr オブジェクトの属性を設定する
print("*" * 50)
setattr(yamada, "address", "Tokyo")
print(yamada.address)

setattr(yamada,"say_bye", say_bye)
yamada.say_bye()

if not hasattr(yamada, "say_good_night"):
    setattr(yamada, "say_good_night", lambda: print("Good night."))
yamada.say_good_night()


#引数としてインスタンスを渡す
#関連したプロパティとメソッドをひとまとめにして持っている
print("-" * 50)
class Staff:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

John = Staff("John", "課長", 500_000)
Smith = Staff("Smith", "主任", 300_000)

def work(work_name, work_time, staff):
    print(f'{staff.name}は{work_name}を{work_time}時間しました。')
    print(f"{staff.name}は{staff.position}で、給料は{staff.salary}円です。")
    
work("書類作成", 5, John)
print()
work("市場調査", 3, Smith)


class Human:
    def __init__(self, name, age, gender="unknown"):
        self.name = name
        self.age = age
        self.gender = gender
        
    def say_hello(self):
        print(f'こんにちは。私は{self.name}です。\n年齢は{self.age}です。\n性別は{self.gender}です。')
def say_bye():
    print('さようなら。')


#インスタンス       
yamada = Human(name='Taro Yamada', age=20, gender="Male")
yamada.say_hello()
print(yamada.name, yamada.age, yamada.gender)
yamada.address = 'Tokyo'
print(yamada.address)
yamada.say_bye = say_bye
yamada.say_bye()



sato = Human(name='Hanako Sato', age=25, gender="Female")
sato.say_hello()
sato.say_bye = say_bye
sato.say_bye()

suzuki = Human(name='Ichiro Suzuki', age=30)
suzuki.say_hello()
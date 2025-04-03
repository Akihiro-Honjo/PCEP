###オブジェクト指向

##多態性
#異なるクラスのオブジェクトが共通のインターフェース（メソッド）を
#持っている場合は同じように操作できる

import random

class Dog:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "ワンワン"
    
class Cat:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "にゃー"

class Bird:
    def __init__(self, name):
            self.name = name
        
    def speak(self):
        return "チュンチュン"
    
class Lion:
    def __init__(self, name):
            self.name = name
    
taro = Dog("タロウ")
tama = Cat("タマ")
pipi = Bird("ピッピ")
leo = Lion("レオ")

# def speak(animal):
#     print(animal.speak())

def speak(animal):
    if hasattr(animal, "speak"):
        print(animal.speak())
    else:
        print(f"{animal.name}はspeakメソッドがありません。")

speak(taro)
speak(tama)
speak(pipi)
speak(leo)

print("-" * 50)

animals =[
    Dog, Cat, Bird, Lion
]

animal = random.choice(animals)
speak(animal("ハナコ"))





##抽象クラス(具体例な実装を持たないメソッド。インスタンス化できない)

from abc import ABC, abstractclassmethod

class AbstractAnimal(ABC):
    @abstractclassmethod
    def sound(self): #抽象メソッド
        pass
    
    def walk(self):
        print("歩く")

class Dog(AbstractAnimal):
    def sound(self): #具象メソッド
        return "わんわん"

class Cat(AbstractAnimal):
    def sound(self): #具象メソッド
        return "にゃーにゃー"

class Duck(AbstractAnimal):
    pass
    

def animal_sound(animal: AbstractAnimal):
    print(animal.sound())

dog = Dog()
cat = Cat()
# duck = Duck()

animal_sound(dog)
animal_sound(cat)
dog.walk()
cat.walk()

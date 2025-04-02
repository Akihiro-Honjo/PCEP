###多重継承

class Human:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def run(self):
        return f"{self.name}が時速{self.speed}kmで走っています。(人間)"
    
    def speak(self, message):
        return f"{self.name}が{message}と言っています。"

class Hose:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def run(self):
        return f"{self.name}が時速{self.speed}kmで走っています。(馬)"
    
    
class Centaur(Hose, Human): #最初に継承したほうが表示される。この場合はHose
    def __init__(self, name, speed):
        super().__init__(name, speed)

taro = Centaur("taro", 15)
print(taro.run())
print(taro.speak("やっほー"))

#もっと詳しく知る場合は「メソッド解決順序 = MRO(Method Resolution Order)」で調べる
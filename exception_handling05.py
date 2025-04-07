##ユーザー定義例外

#負の値が入力されたらエラー
class NegativeValueError(ValueError):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        #return f"NegativeValueError: 負の値が入力されました:{self.value}"
        return f"{self.__class__.__name__}: 負の値が入力されました:{self.value}"

#年齢が未成年ならエラー
class NotAdultError(ValueError):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"{self.__class__.__name__}: 未成年です。:{self.value}"


class Customer:
    def __init__(self, name, age):
        self.name = name
        self._age = self._set_age(age)
            
    @property
    def age(self):
        return self._age
        
    @staticmethod
    def _set_age(age):
        adult_age = 18
        if age < 0:
            raise NegativeValueError(age)
        elif age < adult_age:
            raise NotAdultError(age)
        return age
        
try:
    taro = Customer("taro", 15)
except (NegativeValueError, NotAdultError) as e:
    print(e)
else:
    print(f"{taro.name}さんの年齢は{taro.age}歳です。")


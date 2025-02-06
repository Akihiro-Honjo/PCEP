#enumerate()関数 インデックスをつける
country_list =['India', 'USA', 'Japan', 'Russia', 'China']
for i, country in enumerate(country_list):
    print(i, country)

country_dict = {
    'India':'New Delhi', 
    'USA': 'Washington DC', 
    'Japan': 'Tokyo', 
    'Russia': 'Moscow', 
    'China': 'Beijing'
}
for index, country in enumerate(country_dict):
    print(index, country)
    

#zip()関数 複数のイテラブルをまとめる
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
address_list = ['Man St', 'Maple Ave', 'Broadway']
for name, age, address in zip(names, ages, address_list):
    print(name, age, address)
    

#辞書関連 各要素を取得する
persons = {
    "John":{"age":23,"gender":"male"},
    "Lisa":{"age":28,"gender":"female"},
    "Linda":{"age":32,"gender":"female"}
}
for key in persons.keys():
    print(key, persons[key])
for value in persons.values():
    print(value["age"])
for name , info in persons.items():
    print(name, info)
#辞書のネスト

#辞書の中に辞書
persons ={
    "alice":{
        "age":20,
        "address":"New York",
        "phone":"123456789",
        "email":"sample@sanmple.com",
        "hobby":["reading", "music"]
    },
    "bob":{
        "age":21,
        "address":"LA"
    },
    "taro":{
        "age":22,
        "address":"Tokyo"
    }
}

alice = persons["alice"]
print(alice)
print(alice["age"])
print(alice["hobby"][1])

for name, person in persons.items():
    print(name, person["age"])
    

#リストに辞書
sushi_neta = [
    {"name":"まぐろ", "price":100},
    {"name":"サーモン", "price":150},
    {"name":"えび", "price":80},
    {"name":"いか", "price":70},
]

print(sushi_neta[0]["price"])

for neta in sushi_neta:
    print(neta["name"], neta["price"])
days = ["sun" , "Mon", "Tue", "Wed" , "Thu", "Fri", "Sta"]
for day in days:
    print(day)


names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
for name in names:
    print(name)
    

sushi_dict =[
    {"name": "マグロ", "price":100, "type":"刺身" },
    {"name": "サーモン", "price":100, "type":"刺身" },
    {"name": "えび", "price":100, "type":"刺身" },
    {"name": "いか", "price":100, "type":"刺身" },
    {"name": "たこ", "price":100, "type":"刺身" },
]

for sushi in sushi_dict:
    print(sushi)
    

name_dict = {
    "John":{"age":20, "country": "USA"},
    "BOb":{"age":22, "country": "USA"},
    "Mosh":{"age":30, "country": "Canada"},
    "Sarah":{"age":25, "country": "USA"},
    "Mary":{"age":28, "country": "USA"},
}

for name in name_dict:
    print(name)
    print(name_dict[name]["age"])
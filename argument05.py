#*argsと**kwargsの組み合わせ
def food_report(greet, title, *args, date="明日", restaurant="銀座のレストラン", **kwargs):
    #messagesの最初の2つを表示する
    print(greet + title)
    #contentsの最初の2つを表示する
    print(f'{date}の{restaurant}でのおすすめ料理をお伝えします。')
    
    #残りのmessagesを表示する
    for arg in args:
        print(arg)
    #残りのcontentsを表示する
    for k, v in kwargs.items():
        if k == 'high_rating':
            print(f'高評価の料理:{v}')
        else:
            print(f'注目の料理:{v}')

messages = ("こんにちは。", #位置引数（greet)
            "グルメ情報の時間です。", #位置引数（title)
            #以下は*args
            '都内では寿司が人気ですが、今日は和食に注目しましょう。',
            '銀座にあるこのレストランでは、季節の食材を使った和食が提供されています。',
            'テレビで紹介されたこともあり、予約が取りにくいことで有名です。',
            'このレストランの看板メニューは、ひつまぶしです。',
            '是非一度、訪れてみてください。'
        )
contents = dict(date="今日", #キーワード引数
                restaurant="新宿のレストラン", #キーワード引数
                high_rating="特製天ぷら", #以下は**kwargs
                featured ='刺身の盛り合わせ'
                )
food_report(*messages, **contents)


###特殊引数
# / 位置引数の終わりを示す
# * キーワード専用引数の始まりを示す

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(f"pos1: {pos1}")
    print(f"pos2: {pos2}")
    print(f"pos_or_kwd: {pos_or_kwd}")
    print(f"kwd1: {kwd1}")
    print(f"kwd2: {kwd2}")
f(1, 2, 3, kwd1="key1", kwd2="key2")

#例1
def order_summary(customer_id, order_id, /, item_name, *, quantity=1, price, discount=0):
    print(f"顧客ID: {customer_id}")
    print(f"注文ID: {order_id}")
    print(f"商品名: {item_name}")
    print(f"数量: {quantity}")
    print(f"単価: {price}")
    print(f"割引: {discount * 100}%")
    print(f"合計金額: {price * quantity * (1 - discount):,}円")

order_summary(123, 456, "ハンバーガー", price=300, quantity= 2, discount=0.1)

#例2
def student_details(student_id, first_name, last_name, /, *, age=None, major=None, gpa=None):
    print(f"学生ID: {student_id}")
    print(f"名: {first_name}")
    print(f"姓: {last_name}")
    if age:
        print(f"年齢: {age}")
    if major:
        print(f"専攻: {major}")    
    if gpa:
        print(f"GPA: {gpa}")

student_details(123, "Alice", "Smith", age=20, major="English", gpa=3.5)
student_details(456, "Bob", "Brown",  gpa=3.0)
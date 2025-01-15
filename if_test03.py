'''
あるECサイトの会員ランクの判定、ダイヤモンド会員の判定を行うための条件式を記述してください。

user_point = 5000  # 獲得総ポイント数
acquisition_times = 40  # ポイント獲得回数
has_card = True  # クレジットカード保有しているか

# ↓に条件式を記述してください。:
    print("ダイヤモンド会員です")
elif user_point >= 2000 and acquisition_times >= 15:
    print("プラチナ会員です")
elif user_point >= 700 and acquisition_times >= 7:
    print("コールド会員です")
else:
    print("シルバー会員です")

'''
user_point = 5000  # 獲得総ポイント数
acquisition_times = 40  # ポイント獲得回数
has_card = True  # クレジットカード保有しているか

# ↓に条件式を記述してください。:
if user_point >= 4000 and acquisition_times >= 30 and has_card:
    print("ダイヤモンド会員です")
elif user_point >= 2000 and acquisition_times >= 15:
    print("プラチナ会員です")
elif user_point >= 700 and acquisition_times >= 7:
    print("コールド会員です")
else:
    print("シルバー会員です")

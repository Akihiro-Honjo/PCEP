"""
Q0. 車が法定速度を守っているか判定するプロクラムを作成してください。
    車の速度が法定速度よりも速い場合は「違反」と表示し、
    速度が法定速度以下の場合は「違反ではありません」と表示してください。
"""

car_speed = 80
speed_limit = 60

if car_speed > speed_limit:
    print('違反')
elif car_speed < speed_limit:
    print('違反ではありません')
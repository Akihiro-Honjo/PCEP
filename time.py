import datetime

now = datetime.datetime.now()
print(now)

xmas = datetime.datetime(2024, 12, 25)
print(xmas)

today = datetime.date.today()
print(today)

#10:05
ten =datetime.time(10, 5 ,0)
print(ten)

now = datetime.datetime.now()
now_time = datetime.time(now.hour , now.minute , now.second)
print(now_time)

ten_days_later = now + datetime.timedelta(days=10)
print(ten_days_later)
print(now - datetime.timedelta(hours=2))
print(now - datetime.timedelta(weeks=1 , days=3))

diff =ten_days_later - now - datetime.timedelta(hours=2)
print(diff)
print(diff.days)




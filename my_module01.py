###標準ライブラリ

##reモジュール
#matchは文字列の先頭から、searchは文字列の途中から探す



#calendarモジュール
import calendar
calendar.prmonth(2025,4)


##datetimeモジュール
import statistics
import random

#data = list(range(1000))
data = [random.randint(0,100) for i in range(1000)]

#平均値
mean = statistics.mean(data)
print("平均値",mean)

#中央値
median = statistics.median(data)
print("中央値",median)

#分散
variance = statistics.variance(data)
print("分散",variance)

#標準偏差
stdev = statistics.stdev(data)
print("標準偏差",stdev)


##urllib.requestモジュール
import urllib.request

url = 'https://yahoo.co.jp/'
response = urllib.request.urlopen(url)
#print(response.read())


##unittestモジュール
import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add_positive_number(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_add_negative_number(self):
        self.assertEqual(add(-1, -2), -3)
    
    def test_add_negaposi_number(self):
        self.assertEqual(add(-1, 2), 1)

unittest.main()

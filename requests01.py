import requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
#ビューティフルスープpypiと検索

response = requests.get('https://traylect-09b887e526f5.herokuapp.com/')
print(response.status_code)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.text)
print(soup.h1.text)
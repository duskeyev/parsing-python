from bs4 import BeautifulSoup
import lxml 
import csv
import time
import pandas as pd
import json
import requests

proxies = {
    'https': '52.151.210.204:9000',

    'http': '52.151.210.204:9000'
}
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        # 'Cookie': 'fp=11fa6ff18da1fc58eb98815ba9da0600',
        'Upgrade-Insecure-Requests': '1',
    }
url = 'https://twitter.com/elonmusk'
 
 
response = requests.get(url, headers=headers,proxies=proxies)
print(f'Status Code: {response.status_code}, Content size: {len(response.text)}')
print (response.text)
items = response.text
with open('data.txt', 'w', encoding='utf-8') as f:
        f.write(items)
 
if response.status_code == 200:
 
    soup = BeautifulSoup(response.content, 'lxml')
    
    tweets = soup.find('div', attrs={'aria-label': 'Лента: Посты Elon Musk'}).find_all('article')
    print(tweets)
for each in tweets:
    tweet = each.find('div', class_= 'css-175oi2r r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu' ).findAll('span',class_= 'css-1qaijid r-bcqeeo r-qvutc0 r-poiln3')[3].text 
    print(tweet)
else:
    print("Ошибка при получении данных:", response.status_code)
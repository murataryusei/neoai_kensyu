import urllib
from urllib import request
from bs4 import BeautifulSoup

full_url = 'https://lionmaru.blog/対マリオの攻略ポイント-vipキャラ対策/'
print(urllib.parse.quote(full_url, safe=':/'))
url = 'https://lionmaru.blog/%E5%AF%BE%E3%83%9E%E3%83%AA%E3%82%AA%E3%81%AE%E6%94%BB%E7%95%A5%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-vip%E3%82%AD%E3%83%A3%E3%83%A9%E5%AF%BE%E7%AD%96/' 
response = request.urlopen(url) 
soup = BeautifulSoup(response) 
response.close()

# print(soup)

topstories = soup.find('div', class_='cps-post-main-box') 
print(topstories)
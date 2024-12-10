'''
파일명: Ex18-2-beautifulsoup.py

BeautifulSoup
    Html, XML 등의 마크업 언어를 파싱하는 라이브러리
    ex) <html> 내용 </html>
BeautifulSoup 설치 방법
pip install beautifulsoup4
'''
from http.client import responses

import requests
from bs4 import BeautifulSoup
# https://m.news.nate.com/rank/list?sc=all&p=day&date=20241210
url = 'https://m.news.nate.com/rank/list'
params = {
    'sc' : 'all',
    'p' : 'day',
    'date' : '20241210'
}
response = requests.get(url, params = params)
html = response.text
print(html)
soup = BeautifulSoup(html, 'html.parser')
tit_list = soup.find_all('h2')
for idx,tit in enumerate(tit_list):
    print(f'{idx+1}: {tit.text.strip()}')
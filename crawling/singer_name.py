import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/genre/kpop/ballad/ballad?tabtype=5'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
singers = soup.select('#container section div ul li')

for singer in singers:
    name = singer.select_one('figure figcaption a').text.strip()
    print(name)
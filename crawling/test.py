import requests
from bs4 import BeautifulSoup
#*[@id="container"]/section[1]/div/div[1]/div/ul/li/a/img
url = f'https://music.bugs.co.kr/artist/80120704?wl_ref=list_ar_02'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
images = soup.select(f'#DEFAULT80120704 table tbody tr')[0].select('td')[1].select_one('a img').attrs['src']
albums = soup.select(f'#DEFAULT80120704 table tbody tr')[0].select('td')[4].select_one('a').text
singers_type = soup.select('#contentArea section div div table tbody tr td')[0].text
print(images,albums,singers_type)
#*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[3]/td/a
## 유튜브 링크 --> https://www.youtube.com/results?search_query={}
## 사운드클라우드 -->
# *[@id="contentArea"]/section[1]/div/div[1]/table/tbody/tr[1]/td
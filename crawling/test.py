import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/artist/80108454?wl_ref=list_ar_02'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
sings = soup.select('#DEFAULT80108454 table tbody tr')
for sing in sings:
    sing_name = sing.select_one('th p a').text.strip()
    singer_name = sing.select_one('.artist a').text
    print(singer_name,sing_name)
# *[ @ id = "DEFAULT80108454"] / table / tbody / tr[1] / td[4] / p / a
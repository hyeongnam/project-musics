import requests
from bs4 import BeautifulSoup

genre = {
            'ballad': ['ballad','dance','pop','folk','manidol','girlidol'],
            'rnh': ['hnp','jni'],
            'rns': ['rnb','soul','fnd'],
            'elec': ['elec','club'],
            'rock': ['modern','punk','metal'],
            'jazz': ['vocal','play'],
            'indie': ['rock','modern','hiphop','elec']
}
with open('singers.csv','w', encoding='utf-8') as f:
    for tmp in genre:
        for temp in genre.get(tmp):
            for i in range(1,2):
                url = f'https://music.bugs.co.kr/genre/kpop/{tmp}/{temp}?tabtype=5&sort=default&nation=all&page={i}'
                html = requests.get(url).text
                soup = BeautifulSoup(html, 'html.parser')
                singers = soup.select('#container section div ul li')
                for singer in singers:
                    name = singer.select_one('figure figcaption a').text.strip()
                    link = singer.select_one('figure figcaption a')
                    sing_num = link.attrs['href'].split('/')[4].split('?')[0]
                    f.write(f'{name, sing_num}\n')


url = f'https://music.bugs.co.kr/artist/{}?wl_ref=list_ar_02'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')


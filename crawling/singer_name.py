import requests
from bs4 import BeautifulSoup
import numpy as np

genre = {
            'ballad': ['ballad','dance','pop','folk','manidol','girlidol'],
            'rnh': ['hnp','jni'],
            'rns': ['rnb','soul','fnd'],
            'elec': ['elec','club'],
            'rock': ['modern','punk','metal'],
            'jazz': ['vocal','play'],
            'indie': ['rock','modern','hiphop','elec']
}
sing_num = []
for tmp in genre:
    for temp in genre.get(tmp):
        for i in range(1,2):
            url = f'https://music.bugs.co.kr/genre/kpop/{tmp}/{temp}?tabtype=5&sort=default&nation=all&page={i}'
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            singers = soup.select('#container section div ul li')
            for singer in singers:
                link = singer.select_one('figure figcaption a')
                sing_num.append(link.attrs['href'].split('/')[4].split('?')[0])

lyrics_num = []
with open('sings.csv','w', encoding='utf-8') as f:
    for item in sing_num:
        url = f'https://music.bugs.co.kr/artist/{item}?wl_ref=list_ar_02'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        sings = soup.select(f'#DEFAULT{item} table tbody tr')
        for sing in sings:
            sing_name = sing.select_one('th p a').text.strip()
            singer_name = sing.select_one('.artist a').text
            sing_link = sing.select_one('td:nth-child(3) a')
            lyrics_num.append(sing_link.attrs['href'].split('/')[4].split('?')[0])
            f.write(f'{singer_name},{sing_name}\n')

with open('lyrics.csv','w', encoding='utf-8') as f:
    for tem in lyrics_num:
        url = f'https://music.bugs.co.kr/track/{tem}?wl_ref=list_tr_08_ar'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        lyrics = soup.select_one('.lyricsContainer xmp')
        if lyrics is not None:
            f.write(f'{lyrics.text}\n')
# musics = np.concatenate([sings.csv, lyrics], axis=1)

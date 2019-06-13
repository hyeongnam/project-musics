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
with open('singer_genre.csv','w', encoding='utf-8') as f:
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
                    singer_name = singer.select('figure figcaption a')[0].text.strip().split("(")[0]
                    f.write(f'{tmp},{temp},{singer_name}\n')

lyrics_num = []
with open('sings.csv','w', encoding='utf-8') as f:
    for item in sing_num:
        url = f'https://music.bugs.co.kr/artist/{item}?wl_ref=list_ar_02'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        sings = soup.select(f'#DEFAULT{item} table tbody tr')
        for sing in sings:
            sing_name = sing.select_one('th p a').text.strip().split("(")[0]
            singer_name = sing.select_one('.artist a').text.strip().split("(")[0]
            singers_type = soup.select('#contentArea section div div table tbody tr td')[0].text
            images = soup.select(f'#DEFAULT{item} table tbody tr')[0].select('td')[1].select_one('a img').attrs['src']
            albums = soup.select(f'#DEFAULT{item} table tbody tr')[0].select('td')[4].select_one('a').text
            sing_link = sing.select_one('td:nth-child(3) a')
            lyrics_num.append(sing_link.attrs['href'].split('/')[4].split('?')[0])
            f.write(f'{singer_name},{sing_name},{singers_type},{albums},{images}\n')

with open('lyrics.csv','w', encoding='utf-8') as f:
    for tem in lyrics_num:
        url = f'https://music.bugs.co.kr/track/{tem}?wl_ref=list_tr_08_ar'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        lyrics = soup.select_one('.lyricsContainer xmp')
        sing_name = soup.select_one('#container h1').text.replace("[19금]","").strip().split("(")[0]
        if lyrics is not None:
            ly = lyrics.text.replace("\n", "")
            f.write(f'{sing_name},{ly}\n')
        else:
            ly = '해당 곡은 가사가 없습니다.'
            f.write(f'{sing_name},{ly}\n')
# musics = np.concatenate([sings.csv, lyrics], axis=1)

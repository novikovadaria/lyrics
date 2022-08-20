import requests
import lxml.html
inf = input('Введите автора и название песни через слэш, мау.')
print('Например my chemical romance/burn bright')
l_i = list(inf)
l = len(l_i)
ind = l_i.index('/')
author = []
lyrics = []
for i in l_i[0:ind]:
    author.append(i)

for i in l_i[ind+1:l]:
    lyrics.append(i)

s_l = ''.join(lyrics)
s_a = ''.join(author)
author_final_condition = s_a.replace(' ', '-')
lyrics_final_condition = s_l.replace(' ', '-')
url = f'https://pesni.guru/text/{author_final_condition}-{lyrics_final_condition}'
api = requests.get(url)
tree = lxml.html.document_fromstring(api.text)
text = tree.xpath(
    '//*[@class="arow"]/div//*[@class="songtext"]/text()')
print('\n'.join(text))

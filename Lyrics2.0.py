from bs4 import BeautifulSoup
import requests
import re

def entry(search):
    newkey = search.lower()
    spliting = newkey.split()
    return '_'.join(spliting)

def finding(listkeys,keyword):
    found = []
    index = 1
    keyword = keyword.lower()
    for each in listkeys:
        new = each[1].lower()
        if new.find(keyword)<0:
            index +=1
            continue
        else:
            cache = str(index) + '- '+each[1] 
            found.append(cache)
    if len(found) == 0:
        False
    else:
        return found

def make_dict(music,artist):
    mu,art = list(music) , list(artist)
    dictio = {}
    index=0
    for e in range(1,len(mu)+1): 
        remusic = re.search(r'.*href=\"(.+)\">\n\s*(.*)<',str(mu[index]))
        reartist = re.search(r'.*href=\".+\">\n\s*(.*) <',str(art[index]))
        name = remusic[2] +'==>'+ reartist[1] 
        dictio[name]= remusic[1]
        index += 1
    return dictio

search = entry(input('Name of song : '))
r = requests.get(f'https://www.lyricfinder.org/search/tracks/{search}')
soup = BeautifulSoup(r.text,'html.parser')
result_search_music = soup.find_all('a',class_='song-title-link')
result_search_artist = soup.find_all('a',class_='artist-link')
if len(result_search_music)==0:
    print('Sorry didnt find anything special!')
    exit()
else:
    choices = make_dict(result_search_music,result_search_artist)
selex = {}
show = choices.keys()
index = 1
for key in show:
    selex[f'{index}'] = key
    print(index,'-',key,end='\n')
    index += 1
minichoice = input('Wanna find the artist? (y/n) ')
if minichoice == 'y':
    keyword = input('your keyword? ')
    if not finding(selex.items(),keyword):
        print('Nothing!')
    else:
        for each in finding(selex.items(),keyword):
            print(each)
else:
    pass
select = input('which one? ')
#next section
index0 = selex[select]
nextr = requests.get(choices[index0])
nextsoup = BeautifulSoup(nextr.text,'html.parser')
Lyrics_search = nextsoup.find('div',class_='col-lg-6')
print(Lyrics_search.text)
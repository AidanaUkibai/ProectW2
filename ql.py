import requests
from bs4 import BeautifulSoup

url="https://www.kinopoisk.ru/lists/movies/series-top250/"
r=requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
films = soup.findAll('div', class_='styles_main__Y8zDm styles_mainWithNotCollapsedBeforeSlot__x4cWo')

data = []
col=0
h=0

for fil in films:
    col+=1
    h+=1
    print(col)
    # print(h)
    link = "https://www.kinopoisk.ru" + fil.find('a', class_='base-movie-main-info_link__YwtP1').get('href')
    print(link)
    text1 = fil.find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
    print(text1)
    #     eng_text1=fil.find('span',class_='desktop-list-main-info_secondaryTitle__ighTt').text
    try:
        eng_text1 = fil.find('span', class_='desktop-list-main-info_secondaryTitle__ighTt').text
    except:
        continue
    print(eng_text1)
    year1 = fil.find('span', class_='desktop-list-main-info_secondaryText__M_aus').text.split(',')[1]
    print(year1)
    country = fil.find('div', class_='desktop-list-main-info_additionalInfo__Hqzof').text.split(' ')[0]
    print(country)
    roles = fil.findAll('span', class_='desktop-list-main-info_truncatedText__IMQRP')[1].text
    print(roles)

    data.append([col,h,link, text1, eng_text1, year1, country, roles])


#print(data)
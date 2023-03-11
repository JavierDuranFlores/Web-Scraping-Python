import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = 'https://www.artic.edu/collection?q=clemente%20orozco'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Expresion regular para validar fechas
paterDate = r'([\d]+)(-([\d])+)*'

links = []

artists = []
titles = []
places = []
dates = []
dimesions = []


ul = soup.find('ul', class_='o-pinboard')
li_list = ul.find_all('li', class_='m-listing')
for li in li_list[0:]:
    
    # IF: para aguardar sola las obras de José
    if li.find('span', class_='subtitle').getText().find('José Clemente Orozco') != -1:

        links.append(li.find('a', class_='m-listing__link').get('href'))

        soup = BeautifulSoup(requests.get(li.find('a', class_='m-listing__link').get('href')).content, 'html.parser')
        
        deflist = soup.find('div', class_='o-article__body').find('dl', class_='deflist o-blocks__block')

        artists.append(deflist.find(attrs={'itemprop': 'creator'}).getText().strip())
        titles.append(deflist.find(attrs={'itemprop': 'name'}).getText().strip())
        places.append(deflist.find(attrs={'itemprop': 'locationCreated'}).getText().strip())
        date = deflist.find(attrs={'itemprop': 'dateCreated'}).getText().strip()
        """ A continuacion se hace: primeramente convertir tupla a string luego borrar todo menos
        lo que cumpla con la expresion regular y para finalizar se aguarda en la lista dates """    
        dates.append(" ".join([f"{t[0]}{t[1]}" for t in re.findall(paterDate, date)]))
        
        dimesions.append(deflist.find(attrs={'itemprop': 'size'}).getText().strip())

df = pd.DataFrame({'Artist': artists})
df['Title'] = titles
df['Place'] = places
df['Date'] = dates
df['Dimesions'] = dimesions
df.to_csv('museo.csv', index=False, encoding='utf-8')


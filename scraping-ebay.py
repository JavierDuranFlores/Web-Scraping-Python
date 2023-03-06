import requests
from bs4 import BeautifulSoup
import pandas as pd

precios = []
nombres = []

url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=iphone+14+&_sacat=0&LH_TitleDesc=0&_odkw=iphone+14+pro+max&_osacat=0'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

for var in soup.find_all('li',attrs={'class':'s-item s-item__pl-on-bottom'}):
    aux = var.find('span',attrs={'role':'heading'}).get_text()
    if '14' == (aux.split(maxsplit=3)[2]): 
        nombres.append(var.find('span',attrs={'role':'heading'}).get_text())
        precios.append(var.find('span',class_='s-item__price').get_text())

df = pd.DataFrame({'Nombres': nombres})
df['Precios'] = precios
df.to_csv('ebayIPhone.csv', index=False, encoding='utf-8')



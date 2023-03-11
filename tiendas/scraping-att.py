import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://tienda.att.com.mx/catalogsearch/result/?q=iphone+14'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

precios = []
nombres = []

for li in soup.find('div', class_='search').find('ol', class_='products').find_all('li')[1:]:
    aux = li.find('strong', class_='name').getText()
    if '14' == (aux.split(maxsplit=3)[2]):
        nombres.append(li.find('strong', class_='name').getText().strip())
        precios.append(li.find('span', class_='price').getText())

df = pd.DataFrame({'Nombres': nombres})
df['Precios'] = precios
df.to_csv('attIPhone.csv', index=False, encoding='utf-8')
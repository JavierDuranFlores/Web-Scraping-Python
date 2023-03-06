import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.coppel.com/SearchDisplay?categoryId=&storeId=10151&catalogId=10051&langId=-5&sType=SimpleSearch&resultCatEntryType=2&showResultsPage=true&searchSource=Q&pageView=&pageGroup=Search&beginIndex=0&pageSize=24&searchTerm=iphone+14&authToken=-1002%252CJdh5JVzqovGDGuZIS9A0yAc11LCiDPi1CWNOoTX%252B9xo%253D'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

precios = []
nombres = []

for li in soup.find('div', class_='product_listing_container').find_all('li')[1:]:
    nombre = li.find('p').getText()
    precio = li.find('span', class_='unique_price').getText()
    aux = nombre
    if 'Celular' == (aux.split(maxsplit=1)[0]):
        precios.append(precio.strip())
        nombres.append(nombre)

df = pd.DataFrame({'Nombres': nombres})
df['Precios'] = precios
df.to_csv('coppelIPhone.csv', index=False, encoding='utf-8')

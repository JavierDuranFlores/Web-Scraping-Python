import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://listado.mercadolibre.com.mx/iphone-14#D[A:iphone%2014]'

response = requests.get(url)
nombres = []
precios = []
soup = BeautifulSoup(response.content, 'html.parser')
"""search = soup.find('ol', class_='ui-search-layout')
list_product = search.find_all('li')"""


for product in soup.find('ol', class_='ui-search-layout').find_all('li')[1:]:
    aux = product.find('h2').getText()
    if '14' == (aux.split(maxsplit=5)[2]):
        nombres.append(product.find('h2').getText())
        precios.append(product.find('span', class_='price-tag-fraction').getText())

df = pd.DataFrame({'Nombres': nombres})
df['Precios'] = precios
df.to_csv('mercadoLibreIPhone.csv', index=False, encoding='utf-8')


# Intentos

#item_list = div_list.find('div', class_='s-result-list')
#for div in div_list[1:]:
    #print('Javier\n')
#print(div)
    #print('\n')

"""for item in item_list[1:]:
    title_div = item.find('div', class_='s-title-instructions-style')
    print(item)
    precio_div = item.find('div', class_='s-price-instructions-style')
    title = title_div.find('span', class_='a-text-normal').getText()
    aux = title
    #if 'Apple' == (aux.split(maxsplit=1)[0]):
        #precio = precio_div.find('span', class_='a-offscreen')
    print(title)
        #precios.append(precio.text)
    nombres.append(title)
    #print(title.text)
    #print(precio.text)

df = pd.DataFrame({'Nombres': nombres})
##df['Precios'] = precios
df.to_csv('amazonPreciosIPhone.csv', index=False, encoding='utf-8')
"""
"""span_list_precio = soup.find_all('span', class_='a-offscreen')
span_list_nombre = soup.find_all('span', class_='a-text-normal')


contN = 1
contP = 1
for nombre in span_list_nombre[1:]:
    if nombre.find('14') == 1:
        nombres.append(nombre.text)
        print('{} {}'.format(contN, nombre))
        contN = contN + 1

for precio in span_list_precio[1:]:
        print('{} {}'.format(contP, precio))
    contP = contP + 1

df = pd.DataFrame({'Nombres': nombres})
df['Precios'] = precios
df.to_csv('amazonPreciosIPhone.csv', index=False, encoding='utf-8')
"""
"""
for div in div_list[1:]:
    rows = div.find_all('div', class_='a-row')
    for row in rows[1:]:
        span = row.find('span', class_='a-offscreen')
        print(span)
    ##item_list = div.find('div', class_='s-search-results')
    ##span_list = item_list.find_all('a')
    ##for span in span_list[1:]:
    ##    print(span_list)
    #for item in item_list[1:]:
    #div_row = item_list.find_all('div', clas_='a-row').getText()
    #print("Javier" + item.find('span', class_='a-offscreen').getText())

#print(item)
"""
"""
-----
    rows = item.find_all('div', clas_='a-row')
    for row in rows[1:]:
        precio = row.find('span', class_='a-price').getText()
        precio_final = precio.find('span', class_='a-offscreen').getText()
        print(precio_final)
"""
#for span in span_list[1:]:
#precio = span.find('span', class_='a-offscreen')
#print(span.text)
"""span_list = soup.find_all('p', class_='text_text__3oq-D text_large__K4EIS text_bold__2Ptj-')
    #precio = span.find('div', class_='vtex-product-summary-2-x-currencyInteger').getText()
"""
#item_list = div_list.find('div', class_='itemPLP')

#print(div_list)

"""for item in item_list[1:]:
    nombre = item.find('span').getText()
    print(nombre)
"""

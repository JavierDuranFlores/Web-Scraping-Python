import pandas as pd
import re
import subprocess

subprocess.call('./run.sh')

def solo_numeros(texto):
    numeros = re.sub(r"[^\d.]+", '', texto)
    return numeros


coppelData = pd.read_csv('coppelIPhone.csv')

minIPhone14Coppel = coppelData.sort_values('Precios', ascending=True).head(1)
precioMinCoppel = coppelData['Precios'].min()

mercadoLibreData = pd.read_csv('mercadoLibreIPhone.csv')

minIPhone14MercadoLibre = mercadoLibreData.sort_values('Precios', ascending=True).head(1)
precioMinMercadoLibre = mercadoLibreData['Precios'].min()

attData = pd.read_csv('attIPhone.csv')

minIPhone14Att = attData.sort_values('Precios', ascending=True).head(1)
precioMinAtt = attData['Precios'].min()

ebayData = pd.read_csv('ebayIPhone.csv')

minIPhone14Ebay = ebayData.sort_values('Precios', ascending=True).head(1)
precioMinEbay = ebayData['Precios'].min()

precios = [solo_numeros(precioMinCoppel), solo_numeros(precioMinMercadoLibre), solo_numeros(precioMinEbay), solo_numeros(precioMinAtt)]

precioMin = min(precios)

print('Coppel')
print(minIPhone14Coppel)
print('Mercado Libre')
print(minIPhone14MercadoLibre)
print('AT&T')
print(minIPhone14Att)
print('Ebay')
print(minIPhone14Ebay)

print('\nTienda con menor precio: ')
if precioMin == solo_numeros(precioMinCoppel):
    print('Tienda Coppel')
    print(minIPhone14Coppel)
elif precioMin == solo_numeros(precioMinMercadoLibre):
    print('Tiendad Mercado Libre')
    print(minIPhone14MercadoLibre)
elif precioMin == solo_numeros(precioMinAtt):
    print('Tiendad AT&T')
    print(minIPhone14Att)
elif precioMin == solo_numeros(precioMinEbay):
    print('Tienda Ebay')
    print(minIPhone14Ebay)




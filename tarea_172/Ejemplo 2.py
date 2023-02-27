# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:06:36 2022

@author: igori
"""

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import matplotlib as plt


url = "https://es.wikipedia.org/wiki/Anexo:Monumentos_m%C3%A1s_visitados_del_mundo"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Página recibida OK!")
    data = response.text
else:
    print("Error desde el servidor: " + response.status_code)

# Instanciamos el objeto Beautiful Soup para poder parsear el html:
soup = BeautifulSoup(data, 'html.parser')

# Como esta página contiene más de una etiqueta <table> debemos poder filtrar por algún otro atributo.
# En este caso, con la clase tipo "sortable".
table = soup.find('table', class_='sortable')

# Los nombres de columna (Imagen, Nombre, Ciudad, etc) no están en la primera fila, sino en la segunda
cabecera = table.tbody.find_all('tr')[1]
print(cabecera)

# Generamos un listado con los nombres de las columnas.
tds = cabecera.find_all('td')
columnas = list(map(lambda a:a.text.strip(), tds))


df = pd.DataFrame()
for row_num, row in enumerate(table.tbody.find_all('tr')):
    celdas = row.find_all('td')
    fila = {}
    if(row_num>1 and row_num<80 and celdas != []):
        for idx, celda in enumerate(celdas):
            if idx < len(columnas):
                # Se ignoran las columnas 0, 1, 2 y 8.
                if idx in [0,1,2,8]: #skip
                    pass 
                elif idx == 3: # Nombre
                    # El nombre del monumento se obtiene desde el texto de un enlace <a>.
                    fila[columnas[idx]] = celda.a.text
                elif idx == 5: # Pais
                    # El país se puede encontrar dentro de un enlace ó dentro de un <span>.
                    enlace = celda.find_all("a")
                    try:
                        fila[columnas[idx]] = enlace[1].text
                    except:
                        fila[columnas[idx]] = celda.span.text
                elif idx == 6: #Visitantes
                    # Para el valor de visitantes eliminamos caracteres no numéricos.
                    fila[columnas[idx]] = celda.text.strip().replace('\xa0','').replace('+','')
                else:
                   # Y para el resto de columnas buscamos dentro del contenido.
                    try:
                        fila[columnas[idx]] = celda.contents[0].text.strip()
                    except:
                        fila[columnas[idx]] = celda.text.strip()
        df = df.append(fila, ignore_index=True)
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:42:04 2022

@author: igori
"""

import requests
from bs4 import BeautifulSoup
import json

url = "https://www.toureiffel.paris/es/el-monumento/cifras-clave"

# Indicamos el user-agent (etiqueta con información sobre el dispositivo, para parecer más humanos) como headers.
headers = {'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/98.0.4758.82 Safari/537.36',}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Página recibida OK!")
    # De todo el response nos quedamos solo con el contenido (.text)
    # El "response.text" devuelve todo el código fuente HTML de la página web.
    data = response.text
else:
    print("Error desde el servidor: " + response.status_code)

# Ahora usamos BeautifulSoup para crear un arbol de contenidos tipo html (especificado en el parser).
# Esta estructura permite realizar busquedas de una manera más facil.
# https://j2logo.com/python/web-scraping-con-python-guia-inicio-beautifulsoup/
soup = BeautifulSoup(data, 'html.parser')

table = soup.table
# Filtramos por 'tr', que se refiere al tag para utilizado en html para tablas.
filas = table.tbody.find_all('tr')
nuevo_dict = dict()
for fila in filas:
    # fila contiene cada fila de la tablas (el completo esta en filas).
    # tag 'th' para clave y tag 'td' para cada valor.
    clave = fila.th.text
    valor = fila.td.text
    nuevo_dict[clave] = valor
nuevo_dict


filename = "Output ejemplo 1.json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(nuevo_dict, f, ensure_ascii=False, indent=4)

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:31:18 2020

@author: igori
"""
numerobinario = list()
aux = 0

while aux == 0:
    try:
        numerodecimal = float(input("Introduce un número decimal: "))
        aux = 1
    except ValueError:
        print("Formato de número incorrecto")
        aux = 0

if int(numerodecimal) != numerodecimal:
    aux = True
    numerodespuescoma = numerodecimal - (int(numerodecimal))
else:
    aux = False

numerodecimal = int(numerodecimal)
division = numerodecimal

while division > 1:
    numerobinario.append(division % 2)
    division = division // 2
numerobinario.append(division)
numerobinario.reverse()

if aux is True:
    numerobinario.append('.')
    result = 1
    while result != 0:
        result = numerodespuescoma * 2
        numerobinario.append(int(result))
        numerodespuescoma = result - (int(result))

print('Número equivalente en binario: ',
      (''.join(str(v) for v in numerobinario)))

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
# Mirar lo de las clases
# https://pythones.net/clases-y-metodos-python-oop/
# https://tutorial.recursospython.com/clases/
# https://programacion.net/articulo/como_funcionan_las_clases_y_objetos_en_python_1505

# Convertidor analogico-digital
# https://soundgirls.org/entendiendo-los-convertidores-ad-da/
# https://www.diferenciador.com/sistema-digital-y-sistema-analogico/
# https://bookdown.org/aquintela/EBE/variables-discretas-y-continuas.html
# https://www.youtube.com/watch?v=w1K1InJYZh4
# https://www.youtube.com/watch?v=-4rUKlNeCEs

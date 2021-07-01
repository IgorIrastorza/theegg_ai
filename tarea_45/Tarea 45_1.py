# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:22:03 2021

@author: igori
"""

lista = [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
def particionado (lista):
    pivote = lista[0]
    menores = []
    mayores = []
    
    for i in range(1, len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    pivote = [pivote]
    
    return menores, pivote, mayores

def quicksort (lista):
    if len(lista) < 2:
        return lista 
    menores, pivote, mayores = particionado(lista)
    
    return quicksort(menores) + pivote + quicksort(mayores)

print(quicksort(lista))

# actual versión->>
# https://www.youtube.com/watch?v=3_vD60LQ8Ec
# versión más jodida->>
# https://www.youtube.com/watch?v=I318gmPeDHc
# http://es.tldp.org/Tutoriales/doc-programacion-algoritmos-ordenacion/alg_orden.pdf
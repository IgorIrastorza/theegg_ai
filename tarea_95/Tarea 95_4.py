# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:49:34 2021

@author: igori
"""

numero_1 = 9
numero_2 = 3
numero_3 = 6

# media = numero_1 + numero_2 + numero_3 / 3
# El programa calcula mal la media porque no se usan los parentesis.
# Lo que está haciendo es numero_1 + numero_2 + (numero_3 / 3).
media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)

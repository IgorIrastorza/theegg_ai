# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 17:54:41 2020

@author: igori
"""


import random


def batalla(pok1, pok2):
    turno = random.choice([0, 1])
    while pok1.vida > 0 and pok2.vida > 0:
        if turno == 0:
            pok2.vida = pok2.vida - pok1.ataque
            turno = 1
        else:
            pok1.vida = pok1.vida - pok2.ataque
            turno = 0

    if pok1.vida <= 0:
        print(pok2.nombre, 'es el pokemon ganador!')
    else:
        print(pok1.nombre, 'es el pokemon ganador!')


def main():
    print('- Pokemon número 1')
    pokemon1 = Pokemon()
    print('')
    print('- Pokemon número 2')
    pokemon2 = Pokemon()
    print('--------------------------------------------------------')
    batalla(pokemon1, pokemon2)


class Pokemon:
    def __init__(self):
        self.vida = 100
        self.nombre = input("Introduce el nombre del pokemon : ")
        self.ataque = int(input("Introduce su poder de ataque: "))


main()

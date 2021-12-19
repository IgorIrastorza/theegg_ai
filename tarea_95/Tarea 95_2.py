# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:23:04 2021

@author: igori
"""
import re


def main():
    text_regex = Regex()
    text_regex.character_number()
    text_regex.comparison()


class Regex:
    def __init__(self):
        self.text = input('Introduce el texto a analizar: ')
        self.length = 0

    def character_number(self):
        # Función para calcular el número de caracteres en el texto.
        pattern = re.compile(".")
        self.length = len(pattern.findall(self.text))
        print("___________________________________________________________")
        print("Número de caracteres en el texto:", self.length)

    def comparison(self):
        # Función para hacer la comparación respecto al número 5 y 10.
        if self.length > 5:
            if self.length < 10:
                print('El número de caracteres es mayor que 5 '
                      'pero menor que 10.')
            else:
                print('El número de caracteres es mayor o igual a 10.')
        else:
            if self.length == 5:
                print('El número es igual a 5.')
            else:
                print('El número de caracteres es menor a 5.')


if __name__ == '__main__':
    main()

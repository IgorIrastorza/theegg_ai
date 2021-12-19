# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 19:01:14 2021

@author: igori
"""


def main():
    number = odd_number()
    number.insertion()


class odd_number:
    def __init__(self):
        self.__number = None

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        # Se comprueba si el número introducido es impar.
        try:
            number = int(number)
            if number % 2 != 0:
                self.__number = int(number)
                print('¡Número correcto!')
            else:
                self.__number = None
                print('¡Introduce un número impar!')
        except ValueError:
            self.__number = None
            print('¡Introduce un número en formato valido!')

    def insertion(self):
        # Función para que el usuario inserte los números correspondientes.
        print('Introduce un número impar: ')
        while self.__number is None:
            self.number = input('- ')


if __name__ == '__main__':
    main()

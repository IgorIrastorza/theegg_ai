# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 23:12:58 2021

@author: igori
"""
import pandas as pd


def main():
    multip = multiplication()
    multip.insertion()
    multip.multiplication_table()


class multiplication:
    def __init__(self):
        self.__number = None
        self.__multiplication_table = []

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        # Se comprueba si el número introducido está entre 0 y 99.
        try:
            number = int(number)
            if number >= 0 and number <= 99:
                self.__number = int(number)
            else:
                self.__number = None
                print('¡Introduce un número en formato valido!')
        except ValueError:
            self.__number = None
            print('¡Introduce un número en formato valido!')

    def insertion(self):
        # Función para que el usuario inserte los números correspondientes.
        print('Introduce un número entre 0 y 99: ')
        while self.__number is None:
            self.number = input('- ')

        print('--------------------------------------------------------------')

    def multiplication_table(self):
        # Función para construir el dataframe con la tabla de multiplicaciones.
        dataframe = pd.DataFrame(columns=['Coeficiente 1', 'Coeficiente 2',
                                          'Resultado multiplicación'])
        for i in range(1, 11):
            dataframe.loc[i] = [self.number, i, (self.number * i)]

        print(dataframe)


if __name__ == '__main__':
    main()

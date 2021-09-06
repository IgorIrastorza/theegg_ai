# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:03:00 2021

@author: igori
"""

import re


def main():
    cuenta = Cuenta()
    cuenta.titular = input('Introduce tu nombre: ')
    cuenta.ingresar(input('Introduce la cantidad a ingresar: '))
    cuenta.retirar(input('Introduce la cantidad a retirar: '))
    cuenta.mostrar()


class Cuenta:
    def __init__(self):
        self.__titular = None
        self.__cantidad = 0

    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self, titular):
        # Para validar y escribir el atributo titular.

        # Se importa el modulo regex para validar si el formato del nombre...
        # ...introducido es correcto.
        pattern = re.compile(r'[a-zA-Z]')
        result = pattern.findall(titular)
        if len(result) == len(list(titular)):
            self.__titular = titular
        else:
            print("Formato de nombre incorrecto.")

    def ingresar(self, cantidad):
        # Función para ingresar dinero en la cuenta.
        # Comprueba si el número introducido cumple con el formato.
        try:
            cantidad = float(cantidad)
            if cantidad > 0:
                self.__cantidad = self.__cantidad + cantidad
        except ValueError:
            print('Introduce una cifra correcta')

    def retirar(self, cantidad):
        # Función para retirar dinero en la cuenta.
        # Comprueba si el número introducido cumple con el formato.
        try:
            cantidad = float(cantidad)
            if cantidad > 0:
                self.__cantidad = self.__cantidad - cantidad
        except ValueError:
            print('Introduce una cifra correcta')

    def mostrar(self):
        # Para mostrar los tres atributos.
        print('----------------------------------------------------------')
        print('- Titular de la cuenta:', self.titular)
        print('- Saldo total:', self.cantidad)


if __name__ == '__main__':
    main()

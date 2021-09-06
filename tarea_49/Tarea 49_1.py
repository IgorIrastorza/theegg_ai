# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 21:52:04 2021

@author: igori
"""
import re


def main():
    usuario = Persona()
    usuario.nombre = input('Introduce tu nombre: ')
    usuario.DNI = input('Introduce tu DNI: ')
    usuario.edad = input('Introduce tu edad: ')
    usuario.mostrar()


class Persona:
    def __init__(self):
        self.__nombre = None
        self.__edad = None
        self.__DNI = None

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def DNI(self):
        return self.__DNI

    @nombre.setter
    def nombre(self, nombre):
        # Para validar y escribir el atributo nombre.

        # Se importa el modulo regex para validar si el formato del nombre...
        # ...introducido es correcto.
        pattern = re.compile(r'[a-zA-Z]')
        result = pattern.findall(nombre)
        if len(result) == len(list(nombre)):
            self.__nombre = nombre
        else:
            print("Formato de nombre incorrecto.")

    @edad.setter
    def edad(self, edad):
        # Para validar y escribir el atributo edad.
        try:
            self.__edad = int(edad)
            print('----------------------------------------------------------')
            print('Es mayor de edad:', self.esMayorDeEdad())
        except ValueError:
            print("Formato de edad incorrecto.")

    @DNI.setter
    def DNI(self, DNI):
        # Para validar y escribir el atributo titular.

        # Se importa el modulo regex para validar si el formato del nombre...
        # ...introducido es correcto.
        # La primera busqueda busca si el DNI contiene 8 números.
        pattern = re.compile(r'\d')
        result = pattern.findall(DNI)
        # La segunda busqueda busca si el DNI contiene una letra...
        # ...y la tercera si la letra está en la posición correcta.
        pattern = re.compile(r'[a-zA-Z]')
        result1 = pattern.findall(DNI)
        result2 = pattern.search(DNI)

        if len(result) == 8 and len(result1) == 1 and result2.start() == 8:
            self.__DNI = DNI
        else:
            print('Formato de DNI incorrecto.')

    def esMayorDeEdad(self):
        # Devuelve True si es mayor de edad y False si no lo es.
        if self.edad < 18:
            return False
        else:
            return True

    def mostrar(self):
        # Para mostrar los tres atributos.
        print('----------------------------------------------------------')
        print('- Nombre:', self.nombre)
        print('- Edad:', self.edad)
        print('- DNI:', self.DNI)


if __name__ == '__main__':
    main()

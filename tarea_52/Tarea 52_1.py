# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 22:13:25 2021

@author: igori
"""


def main():
    numbers = numbers_list()
    numbers.insertion()
    numbers.delete()
    numbers.summation()
    numbers.smaller_list()
    numbers.tupla_list()


class numbers_list:
    def __init__(self):
        self.__number = 0
        self.__list = []

    @property
    def number(self):
        return self.__number

    @property
    def list(self):
        return self.__list

    @number.setter
    def number(self, number):
        # Se comprueba si el número introducido es en realidad un número.
        try:
            self.__number = int(number)
        except ValueError:
            self.__number = None
            print('¡Introduce un número en formato valido!')

    def insertion(self):
        # Función para que el usuario inserte los números correspondientes.
        print('Vete introduciendo números y pulsa el enter con cada registro. '
              'Al acabar introduce 0: ')
        while True:
            self.number = input('- ')
            if self.__number == 0:
                break
            else:
                if self.__number is not None:
                    self.__list.append(self.__number)
        print('--------------------------------------------------------------')
        print('Lista de valores: ', self.__list)

    def delete(self):
        # Función para eliminar el elemento que el usuario introduzca...
        # ...de la primera lista creada.
        print('--------------------------------------------------------------')
        print('Introduce un número que hayas insertado en la lista '
              'para eliminarlo:')
        self.number = input('- ')
        try:
            self.list.remove(self.number)
            print('¡Elemento eliminado!')
        except ValueError:
            print('¡No se ha podido eliminar ningún elemento de la lista!')

    def summation(self):
        # Función para hacer una suma de todos los números de la lista.
        result = 0
        for i in range(len(self.__list)):
            result = result + self.__list[i]
        print('--------------------------------------------------------------')
        print('Resultado de la suma de la lista: ', result)

    def smaller_list(self):
        # Esta función crea una nueva lista con números más pequeños...
        # ...al introducido por el usuario.
        print('--------------------------------------------------------------')
        print('Introduce un número para crear una nueva lista con valores '
              'menores: ')
        self.number = input('- ')
        result = []
        if self.__number is not None:
            for i in range(len(self.__list)):
                if self.__list[i] < self.__number:
                    result.append(self.list[i])

        print('Nueva lista creada a partir del número introducido: ',
              (', '.join(str(i) for i in result)))

    def tupla_list(self):
        # Esta función crea una lista de tuplas que contiene...
        # ...el número en cuestión y su frecuencia de aparición.
        unique_list = list(dict.fromkeys(self.__list))
        result = []
        for i in range(len(unique_list)):
            count = 0
            for j in range(len(self.__list)):
                if unique_list[i] == self.__list[j]:
                    count += 1
            result.append((unique_list[i], count))
        print('--------------------------------------------------------------')
        print('Elemento de la lista original y '
              'frecuencia de aparición: ', result)


if __name__ == '__main__':
    main()

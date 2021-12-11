# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 22:37:27 2021

@author: igori
"""


def intersection(set1, set2):
    # Esta función busca los elementos repetidos...
    # ...en los dos conjuntos introducidos.
    intersection = set1 & set2
    if len(intersection) > 0:
        print('Los nombres repetidos en primaria y secundaria '
              'son: ', intersection)
    else:
        print("No hay ningún nombre repetido en primaria y secundaria.")
    print('--------------------------------------------------------------')


def difference(set1, set2):
    # La función busca los elementos que están en el primer conjunto...
    # ...introducido (set1) pero no en el segundo.
    difference = set1 - set2
    if len(difference) > 0:
        print('Los nombres que estan en primaria pero no en secundaria '
              'son: ', (set1 - set2))
    else:
        print('No hay ningún nombre que esté en primaria pero no '
              'en secundaria.')


def main():
    # Función principal del script.
    primary = class_()
    secondary = class_()
    print('INSERTA LOS NOMBRES DE LOS ESTUDIANTES DE PRIMARIA')
    primary.insertion()
    print('INSERTA LOS NOMBRES DE LOS ESTUDIANTES DE SECUNDARIA')
    secondary.insertion()
    intersection(primary.list_names, secondary.list_names)
    difference(primary.list_names, secondary.list_names)


class class_:
    # Clase para crear en este caso las listas de clase.
    def __init__(self):
        self.__list_names = set()

    @property
    def list_names(self):
        return self.__list_names

    def insertion(self):
        # Función para insertar los nombres de la clase.
        print('Vete introduciendo nombres de pila y pulsa enter con cada '
              'registro. Al acabar introduce "?x?": ')
        while True:
            name = input('- ')
            if name == '?x?':
                break
            else:
                if name is not None:
                    self.__list_names.add(name)

        print('Lista de valores: ', self.__list_names)
        print('--------------------------------------------------------------')


if __name__ == '__main__':
    main()

#https://recursospython.com/guias-y-manuales/conjuntos-sets/
#https://www.youtube.com/watch?v=OJRJRxmaLY8
#http://patriciaemiguel.com/ejercicios/python/2019/03/10/ejercicios-estructuras_datos-python.html
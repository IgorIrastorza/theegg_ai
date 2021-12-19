# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 12:08:32 2021

@author: igori
"""


def higherornot(number1, number2):
    # Función para comprobar cual de los números es mayor.
    if number1 > number2:
        print('El primer número introducido es mayor al segundo.')
    else:
        print('El segundo número introducido es mayor al primero.')


def sameornot(number1, number2):
    # Función para comprobar si los números introducidos son iguales o no.
    if number1 == number2:
        print('Los números introducidos son iguales.')
    else:
        print('Los números introducidos son distintos.')
        higherornot(number1, number2)


def insertion():
    # Función para que el usuario inserte el número.
    while True:
        try:
            number = (int(input('Introduce un número: ')))
            break
        except ValueError:
            print("¡Introduzca un formato de número valido! ")

    return number


def main():
    # Función principal del script.
    number1 = insertion()
    number2 = insertion()
    print('------------------------------------------------------------------')
    sameornot(number1, number2)


if __name__ == '__main__':
    main()

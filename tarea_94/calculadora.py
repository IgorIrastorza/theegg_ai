# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 19:35:46 2021

@author: igori
"""


def number(number1, number2):
    # Función para comprobar si los parametros introducidos son números.
    try:
        number1 = float(number1)
        number2 = float(number2)
        return True
    except ValueError:
        print('¡Introduce un número en formato válido!')
        return False


def addition(number1, number2):
    # Función para hacer la suma de dos números.
    # No realiza la operación si uno de los parametros no es número.
    if number(number1, number2) is True:
        return float(number1)+float(number2)


def substraction(number1, number2):
    # Función para hacer la resta de dos números.
    # No realiza la operación si uno de los parametros no es número.
    if number(number1, number2) is True:
        return float(number1)-float(number2)


def multiplication(number1, number2):
    # Función para hacer la multiplicación de dos números.
    # No realiza la operación si uno de los parametros no es número.
    if number(number1, number2) is True:
        return float(number1)*float(number2)


def division(numerator, denominator):
    # Función para hacer la división de dos números.
    # No realiza la operación si uno de los parametros no es número.
    if number(numerator, denominator) is True:
        if denominator == 0:
            print('¡El denominador debe ser distinto a 0!')
        else:
            return float(numerator)/float(denominator)

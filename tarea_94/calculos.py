# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 19:35:46 2021

@author: igori
"""

import calculadora as calc


def main():
    number1 = input('Introduce el primer número: ')
    number2 = input('Introduce el segundo número: ')
    print('-----------------------------------------------------------------')
    print('1. Sumar / 2. Restar / 3. Multiplicar / 4. Dividir')
    action = input('¿Qué desea realizar? Introduzca el número de la acción: ')
    print('-----------------------------------------------------------------')
    if action in ['1', '2', '3', '4']:
        # Dependiendo del número de acción introducido, realiza la llamada...
        # ...a la función correspondiente del módulo 'calculadora'.
        # Si no se introduce un número entre 1 y 4...
        # ...el programa no llamará a ninguna función.
        if action == '1':
            print('Resultado de la suma: ', calc.addition(number1, number2))
        elif action == '2':
            print('Resultado de la resta: ',
                  calc.substraction(number1, number2))
        elif action == '3':
            print('Resultado de la multiplicación: ',
                  calc.multiplication(number1, number2))
        elif action == '4':
            print('Resultado de la división: ',
                  calc.division(number1, number2))
    else:
        print('¡Introduce un número entero de acción entre el 1 y el 4!')


if __name__ == '__main__':
    main()

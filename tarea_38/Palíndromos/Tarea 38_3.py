# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:46:47 2020

@author: igori
"""


def main():
    result = palindrome_prime()
    result.data()
    result.result()


class palindrome_prime:
    def __init__(self):
        self.initial_number = 0
        self.fresult = 0
        self.fresult_inverted = 0

    def data(self):
        # Mientras el número no sea entero ni sea mayor que 1 y menor que...
        # ...1.000.000 el programa estará dentro del bucle
        while self.if_int() is False:
            self.initial_number = input("Introduce un número entero mayor"
                                        " que 1 y menor que 1.000.000: ")

    def if_int(self):
        # Función que devuelve si el número introducido es correcto o no
        try:
            self.initial_number = int(self.initial_number)
            if self.initial_number >= 1 and self.initial_number <= 1000000:
                return True
            else:
                return False
        except ValueError:
            return False

    def result(self):
        # Esta función va probando números desde el inicial hasta que...
        # ...coincide con uno que sea primo y palíndromo
        self.fresult = self.initial_number
        while self.palindrome() is False or self.prime() is False:
            self.fresult += 1
        print("_____________________________________________________________")
        print("Numero palindromo y primo más cercano e igual o mayor que %d: "
              % self.initial_number)
        print(self.fresult)

    def palindrome(self):
        # Esta función devuelve un true si el número es palíndromo y false...
        # ...si no lo es
        self.fresult_inverted = str(self.fresult)
        self.fresult_inverted = list(self.fresult_inverted)
        self.fresult_inverted.reverse()
        self.fresult_inverted = int(''.join(self.fresult_inverted))
        if self.fresult_inverted == self.fresult:
            return True
        else:
            return False

    def prime(self):
        # Esta función devuelve un true si el número es primo y false...
        # ...si no lo es
        n_divisor = 0
        for i in range(1, self.fresult+1):
            if self.fresult % i == 0:
                n_divisor += 1
            if n_divisor > 2:
                break
        if n_divisor == 2:
            return True
        else:
            return False


main()

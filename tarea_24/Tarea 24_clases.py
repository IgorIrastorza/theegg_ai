# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 20:49:34 2020

@author: igori
"""


def main():
    numerobinario = Binario()
    numerodecimal = Decimal()
    numerodecimal.pedir_numero_decimal()
    numerodecimal.numerocoma()
    numerobinario.decimal_to_binary(numerodecimal)


class Binario:
    def __init__(self):
        self.division = 0
        self.binarray = []
        # Como se declara una variable boleana sin decir si es true o false???
        self.numdespcoma = False

    def decimal_to_binary(self, numerodecimal):
        division = numerodecimal.numdecimal
        while division > 1:
            self.binarray.append(division % 2)
            division = division // 2
        self.binarray.append(division)
        self.binarray.reverse()
        if numerodecimal.sinumdespcoma is True:
            self.binarray.append('.')
            result = 1
            while result != 0:
                result = numerodecimal.despuescoma * 2
                self.binarray.append(int(result))
                numerodecimal.despuescoma = result - (int(result))
        print('Número equivalente en binario: ',
              (''.join(str(v) for v in self.binarray)))


class Decimal:
    def __init__(self):
        self.numdecimal = 0
        self.despuescoma = 0
        self.sinumdespcoma = False

    def pedir_numero_decimal(self):
        aux = 0
        while aux == 0:
            try:
                self.numdecimal = float(input("Introduce un número decimal: "))
                aux = 1
            except ValueError:
                print("Formato de número incorrecto")
                aux = 0

    def numerocoma(self):
        if int(self.numdecimal) != self.numdecimal:
            self.sinumdespcoma = True
            self.despuescoma = self.numdecimal - (int(self.numdecimal))
        else:
            self.sinumdespcoma = False
        self.numdecimal = int(self.numdecimal)


main()

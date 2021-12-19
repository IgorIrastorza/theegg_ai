# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 20:18:14 2021

@author: igori
"""


def main():
    suma = 0
    for i in range(0, 116):
        if i % 2 != 0:
            suma = suma + i

    print('Resultado de la suma de los números impares '
          'desde 0 hasta 115: ', suma)


if __name__ == '__main__':
    main()

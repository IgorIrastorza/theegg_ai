# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 21:52:04 2021

@author: igori
"""
import random
import string
import sys
import pandas as pd


def main():
    message = LZ77()
    # text = ['c', 'a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a', 'r', 'r', 'a', 'r', 'r', 'a', 'd']
    text = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a', 'r', 'r', 'a', 'y']
    # for i in range(30):
        #text.append(random.choice(string.ascii_letters+string.digits))
    message.text = text
    message.LZ77_compression()
    message.LZ77_decompression()


class LZ77:
    def __init__(self):
        self.__text = []
        self.__compressed = pd.DataFrame(columns=['m', 'n', 's'])

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        if type(text) == list and len(text) <= 30:
            self.__text = text
            # esto igual ponerlo en la funcion main
            self.string_space(self.__text)
        else:
            print('Debes introducir una variable tipo lista y menor o igual a 30 caracteres')

    def string_space(self, text):
        print('- Espacio que ocupa en bytes:', sys.getsizeof(text))
        print('- Espacio que ocupa en longitud de caracteres:', len(text))

    def LZ77_compression(self):
        buffer = []
        
        print('Hasta la 7. iteración del turko funciona dpm. Sigue comprobando aber!! Animo Igor:)')
        print('En el 8. paso hace una cosa rara el turko (adaptive coding). Miralo y Animo Igor:)')
        
        # i = contador principal para el texto
        # j = contador principal para el buffer
        # aux = contador secundario para cadena larga en texto
        # aux1 = contador secundario para cadena larga en buffer
        i = 0
        #for i in range(0, len(self.__text), (best_result)[1]+1):
        while i < len(self.__text):
            j = len(buffer)-1
            best_result = [0, 0, None]
            s = None
            while j >= 0:
                n = 0
                if self.__text[i] == buffer[j]:
                    m = len(buffer)-j
                    n += 1
                    aux = i+1
                    aux1 = j+1
                    try:
                        # Busca una cadena más larga que un caracter
                        while self.__text[aux] == buffer[aux1]:
                            n += 1
                            aux += 1
                            aux1 += 1
                    except IndexError:
                        # Para cuando llega al final de la lista
                        pass

                    if n > best_result[1]:
                        # Para que guarde el mejor resultado hasta ahora
                        s = self.__text[aux]
                        best_result = [m, n, s]
                j -= 1

            if s is None:
                # Para cuando no se encuentra ningun caracter igual en el buffer
                m = 0
                n = 0
                best_result = [m, n, self.__text[i]]

            buffer.extend(self.text[i:(i+1+best_result[1])])

            # https://es.acervolima.com/2021/02/09/como-agregar-una-fila-en-un-pandas-dataframe-existente/
            self.__compressed.loc[len(self.__compressed.index)] = best_result

            i = i+1+best_result[1]

        self.string_space(self.__compressed)
        print(self.__compressed)

    def LZ77_decompression(self):
        result = []
        y = self.__compressed
        for i in range(len(self.__compressed)):
            if self.__compressed['m'][i] != 0:
                pos = len(result)-(self.__compressed['m'][i])
                result.extend(result[pos:(pos+self.__compressed['n'][i])])
            result.append(self.__compressed['s'][i])
        self.string_space(result)
        print(result)

# https://www.youtube.com/watch?v=y3xSuPDvpOE
# https://www.youtube.com/watch?v=cSyK2iCqr4w


if __name__ == '__main__':
    main()

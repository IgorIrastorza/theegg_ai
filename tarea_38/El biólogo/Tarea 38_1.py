# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:44:02 2020

@author: igori
"""


def main():
    result = SecADN()
    result.data()
    result.largest_sec()


class SecADN:
    def __init__(self):
        self.ADNsecuence1 = []
        self.ADNsecuence2 = []
        self.result_prov = []
        self.fresult = []

    def data(self):
        sec1 = (input("Introduce la primera secuencia de ADN: "))
        sec2 = (input("Introduce la segunda secuencia de ADN: "))
        self.ADNsecuence1 = list(sec1)
        self.ADNsecuence2 = list(sec2)

    def largest_sec(self):
        # sec1_cont será el principal contador del problema. Recorrerá la...
        # ...primera secuencia y indicará el progreso de las verificaciones.
        # Cuando sec1_cont llege al final de sec1, se acabo el problema.
        for sec1_cont in range(len(self.ADNsecuence1)):
            # El sec2_cont recorrerá la segunda secuencia en cada verificación.
            # Se reiniciará cada vez que sec1_cont se mueva
            sec2_cont = 0
            while sec2_cont in range(len(self.ADNsecuence2)):
                # sec1_aux recorrerá la primera secuencia solo cuando...
                # se encuentren cadenas iguales en ambas secuencias.
                sec1_aux = sec1_cont
                self.result_prov = []
                while sec2_cont < len(self.ADNsecuence2)\
                        and sec1_aux < len(self.ADNsecuence1)\
                        and self.ADNsecuence1[sec1_aux] == (self.ADNsecuence2
                                                            [sec2_cont]):
                    self.result_prov.append(self.ADNsecuence1[sec1_aux])
                    sec1_aux += 1
                    sec2_cont += 1
                if len(self.result_prov) >= len(self.fresult):
                    self.fresult = self.result_prov
                sec2_cont += 1

        print('')
        print('_________________________________________________________')
        print('')
        print('Secuencia ADN común más larga: ',
              (''.join(str(i) for i in self.fresult)))


main()

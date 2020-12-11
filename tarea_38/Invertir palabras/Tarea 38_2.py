# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:02:47 2020

@author: igori
"""


def main():
    result = Reverse()
    result.data()
    result.fprint()


class Reverse:
    def __init__(self):
        self.message = []
        self.fresult = []

    def data(self):
        nmessages = int(input("Introduce el número de mensajes: "))
        for i in range(nmessages):
            self.message = [" "]
            self.message.extend(list(input("Introduce el mensaje %d: "
                                           % (i+1))))
            # se guarda la frase invertida devuelta en una...
            # ...única posición del array
            self.fresult.append(self.reverse_order(i))

    def reverse_order(self, i):
        message_inverted = ["Case #%d: " % (i+1)]
        posf = len(self.message)-1
        # aux recorrerá todo el mensaje desde el final hasta el principio
        aux = posf
        while aux >= 0:
            # el espacio indicará cuando acaba y empieza una palabra
            # cuando se encuentre un espacio, se procede a invertir el orden
            # para ello se usa un nuevo array suplementario
            if self.message[aux] == " ":
                message_inverted.extend(self.message[(aux+1):(posf+1)])
                message_inverted.append(" ")
                posf = aux-1
            aux -= 1
        result = ''.join(message_inverted)
        # se devuelve la frase invertida en modo string
        return result

    def fprint(self):
        # se imprime el resultado final
        print("_____________________________________________________________")
        for i in range(len(self.fresult)):
            print(self.fresult[i])


main()

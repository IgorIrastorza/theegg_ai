# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:24:15 2021

@author: igori
"""
import re
import operator


def main():
    text_regex = Regex()
    text_regex.data()
    text_regex.character_number()
    text_regex.word_frequency()


class Regex:
    def __init__(self):
        self.text = ""
        self.pattern = ""
        self.search_result = []

    def data(self):
        # Función para introducir el nombre del archivo y leerlo.
        while True:
            try:
                file_name = (input("Introduce el nombre del archivo: "))
                self.text = open(file_name, encoding='utf-8')
                break
            except FileNotFoundError:
                print("¡Introduzca un nombre de archivo valido y existente en"
                      " la misma ubicación que este archivo! ")
        self.text = self.text.read()

    def character_number(self):
        # Función para calcular el número de caracteres en el texto.
        self.pattern = re.compile(".")
        self.search_result = self.pattern.findall(self.text)
        print("___________________________________________________________")
        print("Número de caracteres en el texto:", len(self.search_result))

    def word_number(self):
        # Función para calcular el número de palabras en el texto.
        self.pattern = re.compile(r'\w+')
        self.search_result = self.pattern.findall(self.text)
        print("___________________________________________________________")
        print("Número de palabras en el texto:", len(self.search_result))

    def word_frequency(self):
        # Función para calcular la frecuencia de uso por palabras en el texto.
        # Primero se construye una columna con todas las palabras del texto.
        self.word_number()
        self.search_result = self.pattern.findall(self.text.upper())
        words = list(set(self.search_result))
        frequency = []
        # Ahora se calcula cuantas veces se repite cada palabra.
        for i in range(len(words)):
            self.pattern = re.compile(r"[^\w]%s[^\w]" % words[i],
                                      re.IGNORECASE)
            frequency.append(len(self.pattern.findall(self.text)))

        result = dict(zip(words, frequency))
        result = sorted(result.items(), key=operator.itemgetter(1),
                        reverse=True)
        print("___________________________________________________________")
        print("Ranking top 10 de palabras por frecuencia de uso:")
        for i in range(0, 10):
            print("%s: %s" % (result[i][0], result[i][1]))


main()

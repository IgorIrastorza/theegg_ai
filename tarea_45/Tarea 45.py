# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:24:15 2021

@author: igori
"""
import pandas as pd
import random
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})


def main():
    search = Search()
    search.order()
    search.sequential_search()
    search.binary_search()
    search.print()
    search.algorithm_performance(0)
    search.algorithm_performance(0.2)
    search.algorithm_performance(0.7)


class Search:
    def __init__(self):
        self.list = [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
        self.list_orden = []
        self.number = 874
        self.iteration_seq = 0
        self.iteration_bin = 0

    def partition(self, lista):
        # Siendo parte del algoritmo quicksort, particiona las listas en...
        # ...menores y mayores comparandolo con el pivote.
        pivot = lista[0]
        minor = []
        major = []

        for i in range(1, len(lista)):
            if lista[i] < pivot:
                minor.append(lista[i])
            else:
                major.append(lista[i])
        pivot = [pivot]

        return minor, pivot, major

    def quicksort(self, lista):
        # Algoritmo de ordenación quicksort para ordenar la lista introducida.
        if len(lista) < 2:
            return lista
        minor, pivot, major = self.partition(lista)

        return self.quicksort(minor) + pivot + self.quicksort(major)

    def order(self):
        # Función de llamada del main para ordenar el array.
        print("Lista sin ordenar: ", self.list)
        self.list_orden = self.quicksort(self.list)
        print("Lista ordenada: ", self.list_orden)
        print("-------------------------------------------------------------")

    def sequential_search(self):
        # Función para buscar un elemento del array siguiendo el...
        # ...método secuencial.
        self.iteration_seq = 0
        for index in range(len(self.list_orden)):
            self.iteration_seq += 1
            if self.list_orden[index] == self.number:
                break

    def binary_search(self):
        # Función para buscar un elemento del array siguiendo el...
        # ...método binario.
        self.iteration_bin = 0
        init = 0
        fin = len(self.list_orden) - 1

        while True:
            mid = int((init + fin) / 2)
            self.iteration_bin += 1
            if self.list_orden[mid] == self.number:
                break
            if self.list_orden[mid] < self.number:
                init = mid + 1
            else:
                fin = mid - 1

    def print(self):
        # Imprime los resultados de las busquedas.
        print("BUSQUEDA SECUENCIAL (%d)" % self.number)
        print("Número de iteraciones:", self.iteration_seq)
        print("BUSQUEDA BINARIA (%d)" % self.number)
        print("Número de iteraciones:", self.iteration_bin)
        print("-------------------------------------------------------------")

    def algorithm_performance(self, position):
        # Función para el análisis BIG 0. Crea arrays aleatorios y luego...
        # ...va guardando los resultados obtenidos de...
        # ...iteraciones y tamaños en una matriz.
        print("- Análisis BIG O para la búsqueda en la posición %s/1:"
              % position)
        dataframe = pd.DataFrame(
            columns=['length', 'sequential_iteration', 'binary_iteration'])

        for i in range(100):
            self.list = []
            for j in range(random.randint(10, 500)):
                self.list.append(random.randint(0, 1000))
            self.list_orden = self.quicksort(self.list)
            self.number = self.list_orden[int((len(self.list_orden))*position)]
            self.sequential_search()
            self.binary_search()
            result = dict(length=[len(self.list_orden)],
                          sequential_iteration=[self.iteration_seq],
                          binary_iteration=[self.iteration_bin])
            dataframe = dataframe.append(pd.DataFrame(
                result, index=None), ignore_index=True)

        self.plot(position, dataframe)

    def plot(self, position, dataframe):
        # Grafica los resultados obtenidos en la función anterior para...
        # ...el análisis Big 0.
        ax = dataframe.plot.scatter(x='length', y='sequential_iteration',
                                    figsize=(6, 4), label="Sequential",
                                    color="DarkBlue", title='Análisis BIG O',
                                    xlabel='Length',
                                    ylabel='Number of iterations',
                                    fontsize=10, rot=0)
        dataframe.plot.scatter(x='length', y='binary_iteration',
                               xlabel='Length', ylabel='Number of iterations',
                               label="Binary", color="DarkGreen", ax=ax)
        plt.savefig('plot_bigO_%s.png' % position)


if __name__ == '__main__':
    main()

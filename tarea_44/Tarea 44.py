# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:24:15 2021

@author: igori
"""
import time


def main():
    sum_result = Sum()
    sum_result.data()


class Sum:
    def __init__(self):
        self.number = 1000000
        self.result1 = 0
        self.result2 = 0
        self.time1 = 0
        self.time2 = 0

    def data(self):
        # Está función va ejecutando las funciones y cambiando el número n
        for j in range(4):
            self.sum_linear()
            self.sum_constant()
            self.print()
            self.number *= 10

    def sum_linear(self):
        # Está función ejecuta el algoritmo lineal (Algoritmo 1)
        t0 = time.time()
        for i in range(self.number + 1):
            self.result1 = self.result1 + i
        t1 = time.time()
        self.time1 = t1 - t0

    def sum_constant(self):
        # Está función ejecuta el Método de Gauss (Algoritmo 2)
        t0 = time.time()
        self.result2 = int((self.number / 2) * (self.number + 1))
        t1 = time.time()
        self.time2 = t1 - t0

    def print(self):
        print("for n = %d" % self.number)
        print("%d   -   %s" % (self.result1, self.time1))
        print("%d   -   %s" % (self.result2, self.time2))
        print("_________________________________________________")


main()

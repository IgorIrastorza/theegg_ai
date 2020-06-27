# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:11:25 2020

@author: igori
"""
#Creamos una función para que devuelva un "True" si el número tiene 4 decimales y esta entre 0,0001 y 0,9999 o False si no lo es
def numerocorrecto(x):
    A=int(x*10000)
    B=x*10000
    if A!=B or x>=1 or x==0:
        return False
    else:
        return True

#El programa empieza aqui
x=float(input("Introduce un numero: "))

#Hasta que no introduzca el número correcto estará dentro del bucle
while numerocorrecto(x)==0:
    x=float(input("Introduce un numero entre 0 y 1 y que contenga 4 decimales maximo: "))

#Se encuentra la fracción correspondiente de ese número con denominador=10000
denominador=10000
numerador=0
y=0
R=1
while x!=y:
    numerador=numerador+1
    y=numerador/denominador

A=denominador
B=numerador

#Una vez encontrado la fracción con base 10000, se aplica el algoritmo de Euclides para hallar el MCD entre el divisor y el denominador (10000)
while A!=0 and B!=0:
    D=A//B
    R=A-(B*D)
    A=B
    B=R   
if A>0:
    MCD=A
else:
    MCD=B

#Con el MCD calculado, se divide los dos componentes de la fracción con denominador igual a 10000 para hallar la fracción irreducible
denominador=denominador//MCD
numerador=numerador//MCD
print("La fracción irreducible de ", x, "es ", numerador, "/", denominador)

#https://es.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm


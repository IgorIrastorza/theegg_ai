# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:09:42 2020

@author: igori
"""
#Esta función crea una matriz llena de 0
def creaMatriz (filas,columnas):
    matriz=[]
    for i in range(filas):
        a=[0]*columnas
        matriz.append(a)
    return matriz

#El programa empieza aquí
#Le pedimos al usuario que introduzca los datos y los vamos guardando en arrays y variables
cantidadvacas=int(input("Introduce el número total de vacas que hay en venta: "))
print("")
numvaca=list()
masavaca=list()
prodvaca=list()
capacidadcamion=list()
solucion=list()
print("Ahora introduce los siguientes datos: ")
print("- Masa de la vaca en kg")
print("- Producción de la vaca en litros/día")
print("")
for i in range (cantidadvacas):
    numvaca.append(i+1)
    print ("Vaca número %d" %(i+1))
    masavaca.append(int(input("- ")))
    prodvaca.append(int(input("- ")))
masacamion=int(input("Introduce la masa máxima que puede transportar el camión: "))
for i in range (masacamion+1):
    capacidadcamion.append(i)

#Creamos un nuevo array de peso y producción incluyendo un elemento 0 (0kg, 0 litros/día)
masavaca1=[0]
masavaca1.extend(masavaca)
prodvaca1=[0]
prodvaca1.extend(prodvaca)

#Creamos la matriz con las dimensiones correspondientes para resolver el problema
matrix=creaMatriz(cantidadvacas+1, masacamion+1)

#Aplicamos el algoritmo explicado en el README.md para obtener el resultado óptimo en cada subproblema de la matriz
etapa=1
estado=1
for etapa in range (cantidadvacas+1):
    for estado in range (masacamion+1):
        if masavaca1[etapa]<=capacidadcamion[estado]:
            resta=capacidadcamion[estado]-masavaca1[etapa]
            matrix[etapa][estado]=prodvaca1[etapa]+matrix[etapa-1][resta]
        
        if matrix[etapa][estado]<matrix[etapa-1][estado]:
            matrix[etapa][estado]=matrix[etapa-1][estado]

#Obtenemos el resultado óptimo, que estará en la última etapa y estado
result=matrix[cantidadvacas][masacamion]

#Ahora buscamos cuales son las vacas que irán dentro del camión y las guardamos en un array
etapa=cantidadvacas
estado=masacamion
while etapa>0 and estado>0:
    if matrix[etapa][estado]!=matrix[etapa-1][estado]:
        solucion.append(etapa)
        estado=estado-masavaca1[etapa]
    etapa=etapa-1

#Imprimimos el resultado
aux=len(solucion)-1
print("")
print("-------------------------------------------------------------")
print("")
print("En el camión irán las siguientes vacas:")
while aux>=0:
    pos=numvaca.index(solucion[aux])
    print ("Vaca número %d" %(numvaca[pos]))
    print("- %d kg" %(masavaca[pos]))
    print("- %d litros/día" %(prodvaca[pos]))
    aux=aux-1
print("")
print ("La producción máxima de las vacas que irán en el camión es de %d litros/día " %result)








      
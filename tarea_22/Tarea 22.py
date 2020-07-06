# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:09:42 2020

@author: igori
"""
def creaMatriz (filas,columnas):
    #n filas y y m numero de columnas
    matriz=[]
    for i in range(filas):
        a=[0]*columnas
        matriz.append(a)
    return matriz

#El programa empieza aquí
#Le pedimos al usuario que introduzca los datos y los vamos guardando en arrays y variables
x=int(input("Introduce el número total de vacas que hay en venta: "))
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
for i in range (x):
    numvaca.append(i+1)
    print ("Vaca número %d" %(i+1))
    masavaca.append(int(input("- ")))
    prodvaca.append(int(input("- ")))
masacamion=int(input("Introduce la masa máxima que puede transportar el camión: "))
for i in range (masacamion+1):
    capacidadcamion.append(i)

masavaca1=[0]
masavaca1.extend(masavaca)
prodvaca1=[0]
prodvaca1.extend(prodvaca)

matrix=creaMatriz(x+1, masacamion+1)
cfilas=1
ccolumnas=1

for cfilas in range (x+1):
    for ccolumnas in range (masacamion+1):
        if masavaca1[cfilas]<=capacidadcamion[ccolumnas]:
            resta=capacidadcamion[ccolumnas]-masavaca1[cfilas]
            matrix[cfilas][ccolumnas]=prodvaca1[cfilas]+matrix[cfilas-1][resta]
        
        if matrix[cfilas][ccolumnas]<matrix[cfilas-1][ccolumnas]:
            matrix[cfilas][ccolumnas]=matrix[cfilas-1][ccolumnas]

result=matrix[x][masacamion]
cfilas=x
ccolumnas=masacamion

while cfilas>0 and ccolumnas>0:
    if matrix[cfilas][ccolumnas]!=matrix[cfilas-1][ccolumnas]:
        solucion.append(cfilas)
        ccolumnas=ccolumnas-masavaca1[cfilas]
    cfilas=cfilas-1

aux=len(solucion)-1
print("")
print("-------------------------------------------------------------")
print("")
print("En el camión irán las siguientes vacas:")
#Falta mejorar el final. El como enseñar el resultado al usuario
while aux>=0:
    pos=numvaca.index(solucion[aux])
    print ("Vaca número %d" %(numvaca[pos]))
    print("- %d kg" %(masavaca[pos]))
    print("- %d litros/día" %(prodvaca[pos]))
    aux=aux-1
print("")
print ("La producción máxima de las vacas que irán en el camión es de %d litros/día " %result)

#https://www.youtube.com/watch?v=fVrPwSkSo0I&t=1736s
#https://www.youtube.com/watch?v=j6mmJwogQyI

#matrices
#https://www.youtube.com/watch?v=OyNXw80YgXc
#http://www.cartagena99.com/recursos/alumnos/apuntes/introduccion%20matrices.pdf



#https://www.youtube.com/watch?v=vdVpRjO7g84
#https://leomartinez2019.github.io/python/2017/04/15/programacion-lineal-con-python/
#https://blog.adrianistan.eu/programacion-dinamica-el-problema-de-knapsack







      
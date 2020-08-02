# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:00:52 2020

@author: igori
"""
import random
import re

def mensajeconnumero(mensaje):
    lista=list(mensaje)
    i=0
    while i in range (len(lista)):
        try:
            int(lista[i])
            return True
        except ValueError:
            i+=1
    return False

def sumacarta (simbolocarta, numerocarta):
    global suma_carta
    if simbolocarta=='C':
        suma_carta=numerocarta
    else:
        if simbolocarta=='D':
            suma_carta=numerocarta+13
        else:
            if simbolocarta=='H':
                suma_carta=numerocarta+26
            else:
                if simbolocarta=='S':
                    suma_carta=numerocarta+39
                else:
                    suma_carta=53
    return suma_carta

def sumacarta1 (simbolocarta):
    global suma_carta
    if simbolocarta=='C':
        suma_carta=0
    else:
        if simbolocarta=='D':
            suma_carta=13
        else:
            if simbolocarta=='H':
                suma_carta=0
            else:
                if simbolocarta=='S':
                    suma_carta=13
                
    return suma_carta

def letranumero (mensajeletra):
    #Función para pasar un mensaje de letra a número
    mensajenum=list()
    for i in range (len(mensajeletra)):
        mensajenum.append(alfabetonumero[alfabeto.index(mensajeletra[i])])
    
    return mensajenum

def numeroletra(mensajenumero):
    #Función para pasar de un mensaje de números a letras
    mensajeletr=list()
    for i in range (len(mensajenumero)):
        mensajeletr.append(alfabeto[alfabetonumero.index(mensajenumero[i])])
            
    return mensajeletr 

def generaristra(mensaje, barajanumero, barajasimbolo):
    #Función que genera la ristra correspondiente
    barajanumero = barajanumero[:]
    barajasimbolo = barajasimbolo[:] 
    ristra=list()
    for j in range (len(mensaje)):
        PrimcartaJ=1
        #Paso 1
        while PrimcartaJ==1:
            aux=0
            i=0
            while i in range (len(barajanumero)) and aux==0:
                if barajanumero[i]=='A':
                    aux=barajanumero.pop(i)
                    aux1=barajasimbolo.pop(i)
                    if i==((len(barajanumero))-1):
                        i=0
                    barajanumero.insert((i+1), aux)
                    barajasimbolo.insert((i+1), aux1)
                i+=1
            i=0
            aux=0
            #Paso 2
            while i in range (len(barajanumero)) and aux==0:
                if barajanumero[i]=='B':
                    aux=barajanumero.pop(i)
                    aux1=barajasimbolo.pop(i)
                    if i==((len(barajanumero))-1):
                        i=0
                    if i==((len(barajanumero))-2):
                        i=-1
                    barajanumero.insert((i+2), aux)
                    barajasimbolo.insert((i+2), aux1)
                i+=1
            #Paso 3
            posJ1=barajasimbolo.index('J')
            barajasimbolo.pop(posJ1)
            posJ2=(barajasimbolo.index('J'))+1
            barajasimbolo.insert(posJ1, 'J')
            aux=barajanumero[0:posJ1]
            aux1=barajanumero[posJ1:(posJ2+1)]
            barajanumero=barajanumero[(posJ2+1):54]
            barajanumero.extend(aux1)
            barajanumero.extend(aux)
            aux=barajasimbolo[0:posJ1]
            aux1=barajasimbolo[posJ1:(posJ2+1)]
            barajasimbolo=barajasimbolo[(posJ2+1):54]
            barajasimbolo.extend(aux1)
            barajasimbolo.extend(aux)
            #Paso 4
            valorcarta=sumacarta(barajasimbolo[53], barajanumero[53])
            aux=barajanumero[0:valorcarta]
            aux1=barajanumero[53]
            barajanumero=barajanumero[valorcarta:53]
            barajanumero.extend(aux)
            barajanumero.append(aux1)
            aux=barajasimbolo[0:valorcarta]
            aux1=barajasimbolo[53]
            barajasimbolo=barajasimbolo[valorcarta:53]
            barajasimbolo.extend(aux)
            barajasimbolo.append(aux1)
            #Paso 5 y 6
            valorcarta=sumacarta(barajasimbolo[0], barajanumero[0])
            if barajasimbolo[valorcarta]!='J':
                PrimcartaJ=0
                numletra=barajanumero[valorcarta]+sumacarta1(barajasimbolo[valorcarta])
                ristra.append(alfabeto[numletra-1])
                
    return ristra

def cifrado (mensajeletra, barajanumero, barajasimbolo):
    global ristra
    global ristranum
    suma=list()
    mensajenum=letranumero(mensajeletra)
    ristra=generaristra(mensajeletra, barajanumero, barajasimbolo)
    ristranum=letranumero(ristra)
    for i in range (len(mensajenum)):
        suma.append(ristranum[i]+mensajenum[i])
        if suma[i]>26:
            suma[i]=suma[i]-26
    msjecifrado=numeroletra(suma)
    
    return msjecifrado

def descifrado (mensajecifrado, barajanumero, barajasimbolo):
    global ristra
    global ristranum
    resta=list()
    mensajecifradonum=letranumero(mensajecifrado)
    ristra=generaristra(mensajecifrado, barajanumero, barajasimbolo)
    ristranum=letranumero(ristra)
    for i in range (len(mensajecifradonum)):
            resta.append(mensajecifradonum[i]-ristranum[i])
            if mensajecifradonum[i]<=ristranum[i]:
                resta[i]=resta[i]+26
    msjedescifrado=numeroletra(resta)

    return msjedescifrado
          
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfabetonumero=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
indicesimbolo=['C', 'D', 'H','S']
mensaje=input("Introduce un mensaje: ")
#Hasta que no introduzca ningún número estará dentro del bucle
while mensajeconnumero(mensaje)==True:
    mensaje=input("Si quieres escribir algun número en tu mensaje introducelo en modo texto: ")
#Quitamos espacios y todo lo que no sean palabras del mensaje
mensaje=mensaje.upper()
mensaje=re.sub('[!"@$%/()=?¿¡^`+*.,:;<>_-]', '', mensaje)
mensaje=re.sub('Á', 'A', mensaje)
mensaje=re.sub('É', 'E', mensaje)
mensaje=re.sub('Í', 'I', mensaje)
mensaje=re.sub('Ó', 'O', mensaje)
mensaje=re.sub('Ú', 'U', mensaje)
mensaje=re.sub(' ', '', mensaje)
mensajenumletra=list()
barajanumero=list()
barajasimbolo=list()
mensajeletra= list(mensaje)

#Creación baraja
for i in range (len(indicesimbolo)):
    numcarta=1
    while numcarta<=13:
        barajanumero.append(numcarta)
        barajasimbolo.append(indicesimbolo[i])
        numcarta+=1
barajasimbolo.append('J')
barajasimbolo.append('J')
barajanumero.append('A')
barajanumero.append('B')

#Aleatorización orden baraja
i=random.randint(1,1000000)
random.seed(i)
random.shuffle(barajanumero)
random.seed(i)
random.shuffle(barajasimbolo)

#A continuación se cifra el mensaje introducido usando el algoritmo del solitario
mensajecifrado=cifrado(mensajeletra, barajanumero, barajasimbolo)
print('')
print('')
print('')
print('Mensaje sin cifrar emisor: ', mensaje)
print ('Mensaje cifrado enviado: ', (''.join(mensajecifrado)))
print('======================================================================================')

#Una vez recibido el mensaje cifrado, se descifrará usando la siguiente función:
mensajedescifrado=descifrado(mensajecifrado, barajanumero, barajasimbolo)
print('Mensaje cifrado recibido: ', (''.join(mensajecifrado)))
print('Mensaje descifrado receptor: ',(''.join(mensajedescifrado)))
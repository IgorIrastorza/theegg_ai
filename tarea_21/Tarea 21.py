# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:11:25 2020

@author: igori
"""
#Creamos una función para que devuelva un "True" si el número tiene 4 decimales y esta entre 0,0001 y 0,9999 o False si no lo es
def numerocorrecto(numerointroducido):
    #Primero se comprueba que el caracter introducido sea un número
    try:
        numerointroducido=float(numerointroducido)
    except ValueError:
        return False
    #Ahora se comprueba que el número tenga 4 o menos decimales
    #Para ello el numero entero y con decimales multiplicado por 10000 deberá ser el mismo
    A=int(numerointroducido*10000)
    B=numerointroducido*10000
    if A!=B or numerointroducido>=1 or numerointroducido==0:
        return False
    else:
        return True

#El programa empieza aquí
numerointroducido=input("Introduce un numero: ")

#Hasta que no introduzca el número correcto estará dentro del bucle
while numerocorrecto(numerointroducido)==0:
    numerointroducido=input("Introduce un numero entre 0 y 1 y que contenga 4 decimales maximo: ")
numerointroducido=float(numerointroducido)
#Se encuentra la fracción correspondiente de ese número con denominador=10000
denominador=10000
numerador=0
division=0
residuo=1
while numerointroducido!=division:
    numerador=numerador+1
    division=numerador/denominador

A=denominador
B=numerador

#Una vez encontrado la fracción con base 10000, se aplica el algoritmo de Euclides para hallar el MCD entre el divisor y el denominador (10000)
while A!=0 and B!=0:
    division=A//B
    residuo=A-(B*division)
    A=B
    B=residuo   
if A>0:
    MCD=A
else:
    MCD=B

#Con el MCD calculado, se divide los dos componentes de la fracción con denominador igual a 10000 para hallar la fracción irreducible
denominador=denominador//MCD
numerador=numerador//MCD
print("La fracción irreducible de ", numerointroducido, "es ", numerador, "/", denominador)


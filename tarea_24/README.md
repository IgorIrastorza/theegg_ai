# Tarea 24

## Enunciado
En este ejercicio hay que desarrollar un programa donde una vez enviado un valor decimal a una función
este lo convierta a binario y nos lo devuelva. Se trata de construir un simulador de un convertidor
analógico digital mediante un programa (software).
___

## Solución
El programa ha sido planteado de la siguiente manera:
- Para empezar, el usuario introduce el número decimal que desea convertir.
- El programa comprueba si el formato de numero introducido es correcto y lo clasifica como número decimal con/sin parte fraccional.
- Una vez realizado esto, se aplica el siguiente algoritmo para hacer la conversión:

![Algoritmo a aplicar en cada etapa](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_24/Decimal_Binario.png)

- El usuario recibe el número en binario.

Ejemplo de ejecución del programa:

```
Introduce un número decimal: 1,25
Formato de número incorrecto

Introduce un número decimal: 1.25
Número equivalente en binario:  1.010

```

P.D.: Existe un segundo archivo (Tarea 24_clases.py) con con el código del ejercicio desarrollado usando clases. Los dos archivos funcionan con los mismos input-output y algoritmos de conversión decimal-binario.
___

## Bibliografía
Información detallada sobre los convertidores analógico-digitales:
- https://soundgirls.org/entendiendo-los-convertidores-ad-da/
- https://www.diferenciador.com/sistema-digital-y-sistema-analogico/
- https://bookdown.org/aquintela/EBE/variables-discretas-y-continuas.html

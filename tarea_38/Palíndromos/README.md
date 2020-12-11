# Tarea 38 (Palíndromos)

## Enunciado
Un entero se dice que es un palíndromo si es igual al número que se obtiene al invertir el orden de sus cifras. 
Por ejemplo, 79197 y 324423 son palíndromos. En esta tarea se le dará un entero N, 1 <= N <= 1.000.000. Usted 
debe encontrar el menor entero M tal que M <= N que es primo y M es un palíndromo N.

**Formato de entrada:**
Un solo entero N, (1 <= N <= 1.000.000), en una sola línea.

**Formato de salida:**
Su salida debe consistir en un solo número entero, el más pequeño palíndromo primo mayor que o igual a N.
___

## Solución
El programa ha sido planteado en dos fases:
- En el primer apartado, se comprueba si el número (N) introducido cumple con los requisitos del enunciado: >=1, 
<=1.000.000 Y que sea un número entero.
- En el segundo apartado, una vez introducido un número correcto, se procede a encontrar el número más cercano, que 
siendo igual o mayor que N, sea palindromo y primo a la vez.

El algoritmo general que sigue el programa es el siguiente:

![Algoritmo general](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_38/Pal%C3%ADndromos/diagrama%20de%20flujo_principal.png)
    
La primera comprobación en todos los número sera ver si es palindromo o no siguiendo el siguiente algoritmo (función "palindrome()"): 

![Algoritmo para saber si es palíndromo](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_38/Pal%C3%ADndromos/diagrama%20de%20flujo_pal%C3%ADndromo.png)

Sí el número resulta ser palíndromo, se hará una segunda comprobación mediante otra función
para saber si es primo o no. Se ha asignado este orden de comprobación para optimizar lo máximo posible el programa, ya que 
la cantidad de números palíndromos es menor a la de primos. La función "prime()" se ejecutaría de la siguiente manera:

![Algoritmo para saber si es primo](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_38/Pal%C3%ADndromos/diagrama%20de%20flujo_primo.png)

Ejemplo de ejecución del programa:

```
Introduce un número entero mayor que 1 y menor que 1.000.000: 0

Introduce un número entero mayor que 1 y menor que 1.000.000: 31
_____________________________________________________________
Numero palindromo y primo más cercano e igual o mayor que 31: 
101

```

## Bibliografía
- http://www.nachocabanes.com/retos/reto.php?n=008

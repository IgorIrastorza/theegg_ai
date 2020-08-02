# Tarea 23

## Enunciado
En la siguiente tarea, el alumno debe construir una comunicación cifrada entre dos funciones
utilizando el algoritmo del Solitario:

1.- Una primera función a la que enviemos una variable (que será una frase o cadena e texto) para que la
función lo cifre mediante el Solitario. En programación existen diferentes tipos de variables: strings,
enteros, flotantes, booleanos, ... y en este caso la variable o parámetro que se le envía a la función es de
tipo String.

2.- Una segunda función que recoja el mensaje cifrado y lo descifre utilizando este mismo algoritmo.
___

## Solución
El programa ha sido planteado de la siguiente manera:
- Para empezar, el usuario emisor introduce el mensaje que 
desea enviar y después se guarda y trocea en un array. 
- Una vez realizado esto, se aplica el algoritmo del Solitario (en la bibiliografía aparece un link donde se detalla paso a paso como funciona)
para generar el mensaje cifrado.
- El receptor recibe el mensaje cifrado y lo descifra aplicando también el algoritmo del Solitario.

La clave al aplicar el algoritmo mencionado es la generación de la ristra. Es como la ¨contraseña¨ 
que permite cifrar y descifrar y será necesario que tanto el emisor como el receptor generen la misma ristra. 
Para ello, ambos deberán tener el mismo orden de cartas y seguir los mismos pasos. 

Con el objetivo de que el cifrado sea lo más seguro posible, cada vez que se ejecuta el programa el orden de las cartas cambia aleatoriamente. Además, se eliminan todos los espacios introducidos para que sea imposible adivinar la longitud de las palabras.

Por último, mencionar que el programa también elimina cualquier signo o simbolo que no sea una letra, además de avisar al usuario para que introduzca los números en modo texto.

Ejemplo de ejecución del programa:

```
Introduce un mensaje : domingo 2 de agosto!

Si quieres escribir algun número en tu mensaje introducelo en modo texto : domingo dos de agosto!



Mensaje sin cifrar emisor :  DOMINGODOSDEAGOSTO

Mensaje cifrado enviado :  YHNUKBNFQJVENIJWCN

=========================================================================

Mensaje cifrado recibido :  YHNUKBNFQJVENIJWCN

Mensaje descifrado receptor :  DOMINGODOSDEAGOSTO
                
```
___

## Bibliografía
Información detallada sobre el algoritmo del Solitario:
- https://sindominio.net/biblioweb/telematica/solitario.html
- https://www.youtube.com/watch?v=uxzLm79aSzw&feature=youtu.be

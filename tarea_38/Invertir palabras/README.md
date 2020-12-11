# Tarea 38 (Invertir palabras)

## Enunciado
Dada una serie de palabras separadas por espacios, escribir la frase formada por las mismas palabras en orden inverso. 
Cada palabra estará formada exclusivamente por letras, y existirá exactamente un espacio entre cada pareja de palabras. 
La salida debe ser "Case #" seguido del número de caso, de un símbolo de "dos puntos", de un espacio en blanco y de la frase invertida.

## Solución
La solución planteada en el siguiente problema ha sido resumida en el siguiente diagrama de flujo:

![Algoritmo para invertir el mensaje](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_38/Invertir%20palabras/Diagrama%20de%20flujo%20tarea38_2.png)

La clave para la resolución ha sido identificar los diferentes espacios que ha insertado el usuario en el mensaje. El espacio permite identificar
el principio y final de cada palabra para despues introducirlo en un nuevo array que contendrá el resultado final. Para poder operar con las posiciones
de una forma más sencilla, los mensajes han sido transformados en arrays durante el algoritmo para finalmente convertirse de nuevo en string.

Ejemplo de ejecución del programa:

```
Introduce el número de mensajes: 5

Introduce el mensaje 1: this is a test

Introduce el mensaje 2: the egg.ai

Introduce el mensaje 3: IA

Introduce el mensaje 4: computer

Introduce el mensaje 5: machine learning
_____________________________________________________________
Case #1: test a is this 
Case #2: egg.ai the 
Case #3: IA 
Case #4: computer 
Case #5: learning machine 

```

## Bibliografía
- http://www.nachocabanes.com/retos/reto.php?n=002

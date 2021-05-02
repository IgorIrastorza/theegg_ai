# Tarea 44

## Enunciado
Debes programar el problema que se plantea en la siguiente secuencia de videos en el lenguaje de programación que desees:
1. https://www.youtube.com/watch?v=GD254Gotp-42 
2. https://www.youtube.com/watch?v=MaY6FpP0FEU

## Solución
Los dos videos anteriormente mencionados plantean realizar un programa en el que una vez se introduzca un número n (1.000.000 en este caso), el algoritmo sume todos los números desde 0 hasta n.

Para ello, se han planteado 2 algoritmos distintos, de los que luego se medirá la eficiencia y el término de complejidad O-grande.


- Algoritmo 1: el primer algoritmo ha sido planteado usando el Método de Gauss, en el que se caracteriza la suma de n números de la siguiente manera:

    ![Algoritmo constante](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_44/images/2_Gauss.png)

    Como se observa, una sola operación es suficiente para hacer la suma desde 0 a n, siendo n cualquier número. Por lo tanto, la complejidad de este algoritmo será constante [O(1)].

- Algoritmo 2: este segundo algoritmo consiste en hacer suma manual con cada numero desde 0 hasta n, por lo que tendremos el mismo número de operaciones que el número n:

    ![Algoritmo lineal](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_44/images/1_Lineal.png)

    Eso quiere decir que la complejidad del algoritmo sera lineal [O(n)], manteniendo una relación lineal entre el tamaño del valor de entrada y el tiempo de ejecución.

## Resultados
Los dos algoritmos planteados en la anterior sección han sido ejecutados con cuatro números `n` distintos:
- `n = 1000000`
- `n = 10000000`
- `n = 100000000`
- `n = 1000000000`

Una vez ejecutado el programa, los resultados obtenidos han sido lo siguientes (estos variarán dependiendo del ordenador y del momento en el que se ejecute):

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_44/images/3_Result.png)

La primera linea de cada ejecución es la correspondiente al primer algoritmo lineal y la segunda a la constante, donde la primera columna visualiza el total de la suma y la segunda el tiempo de ejecución necesario para resolver el algoritmo (en segundos).

Como se puede observar, el tiempo de ejecución del primer algoritmo va creciendo en correspondencia con el tamaño del valor que se introduce. Para afirmar si el crecimiento es lineal, se han exportado los datos a un Excel y realizado una regresión lineal:

![Regresión lineal](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_44/images/4_RegresiónLineal.png)

La conclusión es que la regresión lineal es exacta al 100%, con una ecuación lineal `y = 1E-07x + 0,0922` y un R-cuadrado (es una medida estadística de qué tan cerca están los datos de la línea de regresión ajustada) del 100%.

Por otro lado, los tiempos de ejecución del segundo algoritmo (Método de Gauss) se mantienen constantes en todas las ejecuciones (≈0), con tiempos tan pequeños y una exactitud que el paquete instalado `time` y Python no pueden detectarlo. 

## Ejecución del programa

Para ejecutar el programa simplemente hace falta ejecutar el archivo `Tarea 44.py` una vez, sin ninguna interacción con el usuario. Los 4 números están ya introducidos en el programa automáticamente.

## Bibliografía
- https://www.campusmvp.es/recursos/post/Rendimiento-de-algoritmos-y-notacion-Big-O.aspx
- https://medium.com/@charlie_fuentes/notacion-big-0-para-principiantes-f9cbb4b6bec8
- https://elvex.ugr.es/decsai/algorithms/slides/2%20Eficiencia.pdf





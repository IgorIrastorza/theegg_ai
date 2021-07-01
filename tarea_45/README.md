# Tarea 45

## Enunciado
Tenemos la siguiente lista de elementos: [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56].
1. Construye tu propio algoritmo para ordenarlo de menor a mayor.
2. Busca el número 875 utilizando el algoritmo secuencial y el binario. En cada iteración se debe sumar +1 de modo que al final del programa se debe indicar el número de iteraciones realizadas por cada algoritmo hasta encontrar el elemento.
3. Realiza el análisis en Notación Big O (visto en la tarea #44) y describe tu conclusiones en un documento de texto.

## Ordenación de la lista
Para la ordenación de la lista proporcionada en el enunciado se ha utilizado el **algoritmo de Quicksort**.

Se ha escojido este algoritmo por razones de eficiencia, ya que es el algoritmo de ordenación más rápido (en la práctica) conocido hasta ahora. Su tiempo de ejecución promedio es O(n log(n)) y para el peor caso tiene un tiempo O(n^2). El diseño de este algoritmo es fruto de la técnica "divide y vencerás", que se basa en dividir el problema en subproblemas más pequeños.

El algoritmo trabaja de la siguiente forma:

- Elegir un pivote. En este caso, siempre será el primer elemento del array.
- Comparar todos los elementos del array respecto al pivote. Los que son menores se guardan en el array `minor` y los iguales o mayores en el array `major`.
- Se repite este algoritmo recursivamente hasta que la longitud del array `minor` o `major` sea igual o menor a 1.
- Finalmente se unen todas las soluciones óptimas de los subproblemas.


Para el array del enunciado, el funcionamiento del algoritmo sería el siguiente:

![Algoritmo Quicksort](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_45/images/quicksort_algorithm.png)

## Algoritmos de búsqueda

Una vez ordenado el array introducido, se han aplicado dos algoritmos distintos para buscar el número 874. En la siguiente imagen animada se puede observar la diferencia entre los dos métodos:

![Algoritmo secuencial vs binario](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_45/images/binary_sequential.gif)


### Algoritmo secuencial
Consiste en recorrer la lista secuencialmente (desde el inicio hasta el final) comparando cada elemento de la lista con elemento a buscar. Cuando el elemento de la lista sea igual al elemento a buscar, se acaba el algoritmo.

### Algoritmo binario
Este algoritmo funciona fraccionando repetitivamente la lista donde está el elemento a buscar hasta reducir las ubicaciones posibles a solo una. 

Para ello, en cada iteración se selecciona el elemento de la mitad y se compara con elemento a buscar: si el elemento medio es mayor, se selecciona el fragmento de la derecha; si es menor, se selecciona el fragmento de la izquierda; si los dos elementos son iguales, se acaba el algoritmo.

## Resultados
En este caso, la ejecución del programa con el array del enunciado ha dado como resultado las siguientes iteraciones con cada uno de los algoritmos de busqueda:

`Lista sin ordenar:  [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]`

`Lista ordenada:  [3, 21, 23, 33, 45, 56, 56, 65, 66, 123, 874, 1000]`

`-------------------------------------------------------------`

`BUSQUEDA SECUENCIAL (874)`

`Número de iteraciones: 11`

`BUSQUEDA BINARIA (874)`

`Número de iteraciones: 3`

##  Análisis Big O

Una vez realizado la principal tarea del ejercicio, se ha procedido a valorar y comparar la eficiencia de los algoritmos de busqueda binaria y secuencial mediante el análisis Big O.

Para ello, se han construido 100 listas de números distintos de un tamaño aleatorio entre 10 y 500 posiciones. Después, se han realizado 3 tipos de busquedas:

- Búsqueda del número en primera posición del array.

![Posición 0](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_45/plot_bigO_0.png)

- Búsqueda del número en la posición 1/5 del array.

![Posición 0.2](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_45/plot_bigO_0.2.png)
- Búsqueda del número en la posición 7/10 del array.

![Posición 0.7](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_45/plot_bigO_0.7.png)

Como se observa en las gráficas, la complejidad del algoritmo secuencial es lineal [O(n)], dependendiente de la posición del número a buscar (y en consecuencia del tamaño del array). Su rendimiento es superior al binario solo cuando la posición del número a buscar es muy al principio.

Al contrario, cuando se aleja la posición del número a buscar y crece el tamaño del array, la eficiencia del algoritmo binario se mantiene constante, mientras que el secuencial crece linealmente.

## Ejecución del programa

Para ejecutar el programa simplemente hace falta ejecutar el archivo `Tarea 45.py` una vez, sin ninguna interacción con el usuario. El programa también generará tres gráficas (análisis Big O) en formato `png` que serán guardadas en el mismo repositorio del código.

## Bibliografía
- https://www.campusmvp.es/recursos/post/Rendimiento-de-algoritmos-y-notacion-Big-O.aspx
- https://medium.com/@charlie_fuentes/notacion-big-0-para-principiantes-f9cbb4b6bec8
- https://elvex.ugr.es/decsai/algorithms/slides/2%20Eficiencia.pdf
- https://www.youtube.com/watch?v=3_vD60LQ8Ec
- http://es.tldp.org/Tutoriales/doc-programacion-algoritmos-ordenacion/alg_orden.pdf
- https://es.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search
- https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
- https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#from-a-list-of-dicts
- https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#plotting-directly-with-matplotlib





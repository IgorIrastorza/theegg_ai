# Tarea 38 (El biologo)

## Enunciado
Eres un biólogo que examina secuencias de ADN de formas de vida diferentes. Se te darán dos secuencias de ADN, y el objetivo es encontrar 
el conjunto ordenado de bases adyacentes de mayor tamaño que es común en ambos ADNs.

Las secuencias de ADN se darán como conjuntos ordenados de bases de nucleótidos: adenina (abreviado A), citosina (C), guanina (G) y timina (T):

ATGTCTTCCTCGA TGCTTCCTATGAC

Para el ejemplo anterior, el resultado es CTTCCT porque que es el conjunto ordenado de bases adyacentes de mayor tamaño que se encuentra en ambas formas de vida.

## Solución
La primera parte del programa consistirá en que el usuario introduzca las dos secuencias de ADN. Para facilitar el posterior análisis de las secuencias, 
las dos secuencias serán reconvertidas en arrays. Por ejemplo:
- **Secuencia 1**: ctgactga
- **Secuencia 2**: actgagc

La transformación a arrays quedaría de la siguiente manera:

| POSICIÓN | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| -- | -- | -- | -- | -- | -- | -- | -- | -- |
| **SEC 1** | c | t | g | a | c | t | g | a |

| POSICIÓN | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| -- | -- | -- | -- | -- | -- | -- | -- |
| **SEC 2**  | a | c | t | g | a | g | c |

Para recorrer los dos arrays y hacer las comprobaciones se usarán tres contadores distintos:
- **sec1_cont**: será el principal contador del problema. Recorrerá la primera secuencia y indicará el progreso de las verificaciones.
Cuando sec1_cont llege al final de la secuencia 1, se acabo el problema.
- **sec2_cont**: recorrerá la segunda secuencia en cada verificación. Se reiniciará cada vez que sec1_cont se mueva.
- **sec1_aux**: recorrerá la primera secuencia solo cuando se encuentren cadenas iguales en ambas secuencias.

Cuando se este identificando una cadena común en las dos secuencias, se irá guardando el resultado en un nuevo array denominado *result_prov*.
Una vez acabada la secuencia, se comprobará si su longitud es mayor a la registrada anteriormente, y si es así, se guardará en el array 
*fresult* como mejor resultado provisional.

La solución planteada en el problema a partir de la introducción de las dos secuencias también ha sido resumida en el siguiente diagrama de flujo:

![Algoritmo para encontrar la secuencia común más larga](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_33/diagrama%20de%20flujo_tarea33.png)

Ejemplo de ejecución del programa:

```
Introduce la primera secuencia de ADN: ctgactga

Introduce la segunda secuencia de ADN: actgagc

_________________________________________________________

Secuencia ADN común más larga:  actga 

```

## Bibliografía
- http://www.nachocabanes.com/retos/reto.php?n=005

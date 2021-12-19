# Tarea 52

## Enunciado
Los ejercicios propuestos para que el alumno entienda la estructura de datos son los siguientes:
1. Desarrolla un programa que sirva para:
   - Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el
número 0, el cual no debe guardarse.
   - A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su
primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
   - Recorrer la lista para imprimir la sumatoria de todos los elementos.
   - Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores
que el número dado. Imprimir esta nueva lista, iterando por ella.
   - Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)].
2. Desarrolla un programa que sirva para:
   - Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ?x?.
   - A continuación, solicitar que ingrese los nombres de los alumnos de nivel
secundario, finalizando al ingresar ?x?.
   - Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
   - Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
   - Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

## Definición de los conceptos
La comprensión de los tipos de estructura de datos y sus principales conceptos están desarrollados y definidos en el diccionario general disponible en el repositorio `theegg_ai`.

## Ejercicio 1

Para la ejecución del primer ejercicio (`Tarea 52_1.py`) el tipo de estructura de datos usado han sido las listas y tuplas, que pertenecen al grupo de los arrays. Las 4 primeras fases del ejercicio, donde las principales operaciones son inserción, eliminación y busqueda, han sido realizadas usando únicamente listas. Para la última fase, donde se pide la frecuencia de repetición de cada elemento de la lista, se ha combinado la estructura de datos de tuplas con la lista.

Ejemplo de ejecución:

`Vete introduciendo números y pulsa el enter con cada registro. Al acabar introduce 0:`

`- 5`

`- 6`

`- 8`

`- 11`

`- 15`

`- 4`

`- 8`

`- 0`

`--------------------------------------------------------------`

`Lista de valores:  [5, 6, 8, 11, 15, 4, 8]`

`--------------------------------------------------------------`

`Introduce un número que hayas insertado en la lista para eliminarlo:`

`- 4`

`¡Elemento eliminado!`

`--------------------------------------------------------------`

`Resultado de la suma de la lista:  53`

`--------------------------------------------------------------`

`Introduce un número para crear una nueva lista con valores menores: `

`- 10`

`Nueva lista creada a partir del número introducido:  5, 6, 8, 8`

`--------------------------------------------------------------`

`Elemento de la lista original y frecuencia de aparición:  [(5, 1), (6, 1), (8, 2), (11, 1), (15, 1)]`


## Ejercicio 2
En el segundo archivo `Tarea 52_1.py` se encuentra el script para la resolución del segundo problema planteado. Debido a las operaciones que se piden realizar con la lista de datos de los alumnos de primaria y secundaria, la estructura de datos escogida para recojer los datos ha sido el conjunto (set).

Este tipo de estructura, similar en cierta medida a las listas y tuplas, permite realizar operaciones (muy útiles en este caso) como la inserción, la intersección entre listas y la diferencia entre listas. Es por ello que esta estructura de datos resulta adecuada para este ejercicio en concreto.

Ejemplo de ejecución:


`INSERTA LOS NOMBRES DE LOS ESTUDIANTES DE PRIMARIA`

`Vete introduciendo nombres de pila y pulsa enter con cada registro. Al acabar introduce "?x?":`

`- Aitor`

`- Victor`

`- Alberto`

`- ?x?`

`Lista de valores:  {'Aitor', 'Victor', 'Alberto'}`

`--------------------------------------------------------------`

`INSERTA LOS NOMBRES DE LOS ESTUDIANTES DE SECUNDARIA`

`Vete introduciendo nombres de pila y pulsa enter con cada registro. Al acabar introduce "?x?": `

`- Juan`

`- Leo`

`- ?x?`

`Lista de valores:  {'Leo', 'Juan'}`

`--------------------------------------------------------------`

`No hay ningún nombre repetido en primaria y secundaria.`

`--------------------------------------------------------------`

`Los nombres que estan en primaria pero no en secundaria son:  {'Aitor', 'Victor', 'Alberto'}`


## Bibliografía
- https://recursospython.com/guias-y-manuales/conjuntos-sets/
- http://patriciaemiguel.com/ejercicios/python/2019/03/10/ejercicios-estructuras_datos-python.html




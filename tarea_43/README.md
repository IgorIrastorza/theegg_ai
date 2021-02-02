# Tarea 43

En esta tarea se desarrollarán y reportarán distintas consultas SQL realizadas en los retos de la pagina web de https://sqlpd.com/.
___

## Query 1

#### Enunciado
![Enunciado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Sentencia SQL

En este caso, queremos que la consulta realizada seleccione todas las columnas de la tabla mailing_list. Para ello usaremos la expresión `SELECT` seguida de un asterisco, que significa cojer todas las columnas sin excepción:

![Sentencia SQL](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Resultado

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)


## Query 2

#### Enunciado
![Enunciado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Sentencia SQL

En este segundo query el tipo de consulta es la misma que en la anterior:

![Sentencia SQL](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Resultado

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)


## Query 3

#### Enunciado
![Enunciado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Sentencia SQL

En este caso, la consulta no debe seleccionar todas las columnas de la tabla, por lo que será necesario especificar los nombres de esas columnas después de `SELECT`.

![Sentencia SQL](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Resultado

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)


## Query 4

#### Enunciado
![Enunciado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Sentencia SQL

En este query el tipo de consulta es la misma que en la anterior, haciendo una selección filtrada sobre las columnas a buscar:

![Sentencia SQL](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Resultado

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)


## Query 5

#### Enunciado
![Enunciado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Sentencia SQL

En este query, a parte de no seleccionar todas las columnas, se utiliza también el comando `DISTINCT`, que permite eliminar cualquier fila que este duplicada. Si el número de columnas es mayor a 1, el comando solo elimina los duplicados cuando todas las columnas son iguales a los anteriores. El fragmento debe situarse justo después del comando `SELECT`.

![Sentencia SQL](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Resultado

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)


## Query 6

#### Enunciado
![Enunciado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Sentencia SQL

En este sentencia se ha utilizado el comando `ORDER BY`para ordenar la tabla en función de la columna "LastName". Este fragmento de la sentencia debe situarse despúes de `FROM`. Además, permite ordenar tanto en orden ascendente `ASC` como en descendente `DESC`. 

![Sentencia SQL](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Resultado

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)


## Query 7

#### Enunciado
![Enunciado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Sentencia SQL

Similar al anterior query pero en este caso ordenado en modo descendente.

![Sentencia SQL](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Resultado

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)


## Query 8

#### Enunciado
![Enunciado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Sentencia SQL

En este caso se juntan tanto el comando `DISTINCT` como el `ORDER BY` en una única consulta.

![Sentencia SQL](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Resultado

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)


## Query 9

#### Enunciado
![Enunciado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Sentencia SQL

En esta consulta existen dos cláusulas que se deben seguir para ordenar los resultados de la tabla. Esto se escribe separando cada cláusula mediante comas. Al ejecutar el script, se priorizará primero el cumplimiento de la primera condición, luego de la segunda...

![Sentencia SQL](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Resultado

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)


## Query 10

#### Enunciado
![Enunciado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Sentencia SQL

En esta consulta se utiliza, además de las funciones anteriormente comentadas, el operador `LIMIT`, que sirve para limitar el número de registros que devuelve una consulta (20 filas en este caso). El comando se añade después de `ORDER BY`.

![Sentencia SQL](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Resultado

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)


## Query 11

#### Enunciado
![Enunciado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Sentencia SQL

Consulta SQL muy parecida a la décima, con el añadido del comando `DISTINCT` para evitar duplicados en las tablas resultantes.

![Sentencia SQL](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

#### Resultado

![Resultado](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)
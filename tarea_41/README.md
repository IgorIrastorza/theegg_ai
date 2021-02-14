# Tarea 41

## Enunciado
Se debe calcular mediante técnicas de Regex el número de caracteres, el número palabras y ranking de palabras por frecuencia de usodel siguiente texto. La aplicación debe servir para cualquier otro texto:


`"En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar, y hasta cantamos juntos la canción de Annie.Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."`

## Solución
Para resolver este problema de expresiones regulares y procesamiento de textos se ha usado la librería `re` de Python. Este modulo otorga la posibilidad de hacer los siguientes tipos de busqueda en un texto:

- `re.match()`: determina si la regex tiene coincidencias en el comienzo del texto.
- `re.search()`: escanea todo el texto buscando cualquier ubicación donde haya una coincidencia.
- `re.findall()`: encuentra todos los subtextos donde haya una coincidencia y nos devuelve estas coincidencias como una lista.
- `re.finditer()`: es similar al anterior pero en lugar de devolvernos una lista nos devuelve un iterador.

En este caso, como en las tres busquedas se quiere encontrar la cantidad total de cadenas de caracteres que cumplen con un patrón especifico de busqueda, se usará la función `re.findall`. Esta función devolverá una lista con todas las coincidencias encontradas, la cual será procesada mediante la función `len()` para obtener un único resultado final con el número de coincidencias encontradas.

A continuación, los patrones de busqueda planteados para cada parte del problema han sido los siguientes:

#### Calcular el número de caracteres
Para calcular el número de caracteres se ha compilado el siguiente patron de busqueda: `re.compile(".")`. El metacaracter `.` es un delimitador que nos permite delimitar dónde queremos buscar los patrones de búsqueda, que en este caso limita a cualquier caracter en la línea. Por lo tanto, en esta busqueda se buscarán tanto caracteres alfanuméricos como espacios, comas, puntos...

#### Calcular el número de palabras
Para buscar todas las palabras del texto se ha usado el patron de busqueda `re.compile(r'\w+')`, en el cual `\w` indica que el caracter debe ser alfanumérico y `+` que la longitud de la cadena debe ser >=1. Por lo tanto, la función seguirá buscando caracteres alfanuméricos hasta que encuentre un caracter no alfanumérico como espacios, puntos, comas...

#### Ranking de palabras por frecuencia de uso
Para la realización de este apartado se ha aprovechado primero el resultado de la busqueda del calculo de palabras, ya que se ha obtenido un array con todas las palabras que hay en el texto. Como en ese array pueden haber palabras repetidas, se ha usado la función `set()`para eliminar duplicados y obtener todas las palabras "únicas" del texto (guardado en el array `word[]`). 

A continuación,  se ha usado el patrón `re.compile(r"[^\w]%s[^\w]" % words[i], re.IGNORECASE)` para encontrar el número de veces que se repite cada palabra del array `word[]`. Las dos expresiónes `[^\w]` hacen referencia a que cada palabra que queramos buscar (`%s`) debe estar acompañada de caracteres no alfanuméricos (el icono `^` indica que no debe contener) como espacios o puntos. Por último, la expresión `re.IGNORECASE` indica que en la busqueda no debe distinguir entre palabras mayusculas y minusculas.

## Ejecución del programa

Para ejecutar el programa es necesario introducir al principio el nombre del archivo de texto que se desea procesar. El programa te devolverá un error si el nombre del archivo es incorrecto o no se encuentra en la misma ubicación que el programa. El archivo de texto incluido en el repositorio, que corresponde a la tarea a realizar, tiene el nombre `"regex.txt"`.

## Bibliografía
- https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/
- https://docs.python.org/3/library/re.html#module-contents
- https://geekflare.com/es/regular-expression-tester/
- https://platzi.com/blog/expresiones-regulares-python/
- https://relopezbriega.github.io/blog/2015/07/19/expresiones-regulares-con-python/
- http://chuwiki.chuidiang.org/index.php?title=Leer_y_escribir_ficheros_en_python




# Predicción de precios inmobiliarios

## Estado del arte

El primer paso en el desarrollo de un modelo de predicción de precios inmobiliarios será definir más especificamente el alcance del problema. Algunos parametros que se deberían definir son los siguientes:

- Precios de alquiler o compra.
- Tipología del inmueble: nave industrial, parcela, local, garaje, piso...
- Alcance geográfico: global, estatal, autonómico, local.
- Alcance en el tiempo: predicción a un mes, 6 meses, 1 año, 3 años, 5 años...

Cuanto más concretos seamos en la definición del problema, más facil será después obtener un modelo predictivo fiable y útil.

Una vez concretado el problema, se debe definir cuales serán las variables que más impacto tendrán en el precio. No obstante, dependiendo de lo que hayamos definido en el paso anterior, habrá factores que tendrán mayor o menor ponderación en el impacto final del resultado. 

Por ejemplo, si queremos predecir los precios de la vivienda a 3 meses vista en Gipuzkoa, tendrán mucha más importancia los datos de alta frecuencia como el número de pisos actual en oferta y los costes de financiación que los ingresos per capita (dato más macro que tendrá su impacto en un horizonte más largo).

No obstante, los datos que podrían considerarse como input para el modelo son los siguientes:

### Datos concretos del sector inmobiliario
- Oferta de viviendas en venta/alquiler.
- Interes/Demanda en el mercado (por ejemplo, en concepto de visualizaciones en ciertos apartados o busquedas de páginas web concretas como bancos o portales inmobiliarios).
- Número permisos para nueva construcción/reformas.
- Precio m2 venta/alquiler inmuebles (lo que habrá que predecir).

### Datos económicos y políticos
- Evolución del PIB.
- Tasa de inflación. 
- Costes de financiación (intereses de la deuda).
- Ingresos per cápita.
- PIB per cápita.
- Tasa de paro.
- Población.
- Edad media de la población.
- Cantidad total en impuestos.
- Aritmética política actual (autonomías, nacional).
- Riesgo cambios legislativos (aquí habría que tener a una persona/algoritmo de IA valorando el impacto de las noticias de la actualidad política en la compra/venta y alquiler de inmuebles).

## Adquisición de datos
 La mayoria de los datos arriba mencionados podrían obtenerse desde las siguientes referencias: Portales inmobiliarios (Idealista, Fotocasa...), bancos, INE, Eustat, Eurostat.

 Aunque los datos de los organismos públicos estarán disponibles de manera gratuita, los datos referentes a portales inmobiliarios o bancos podrían implicar un coste económico.

 Una explicación más detallada con ejemplos de la comercialización de datos generados en el portal inmobiliario Idealista está disponible en el siguiente [link](https://www.idealista.com/data/ "Idealista Data") o en el apartado bibliográfico de este documento.

## Procedimiento para la resolución del problema

1. Conseguir el historico de los datos arriba mencionados consultando en las correspondientes fuentes.

2. Realizar las hipótesis oportunas para descartar las variables que menos influencia tienen en las variaciones de precios inmobiliarios.

4. Entrenar el modelo siendo la variable objetivo el precio del m2 en el intervalo de tiempo que se haya definido anteriormente. El entrenamiento supervisado se deberá hacer con los datos de unos años atras, dejando por ejemplo el último año conocido para el proceso de testing.

5. Evaluar el rendimiento del modelo construido y volver al primer paso si la eficacia del algoritmo no es lo suficientemente bueno.


## Bibliografía
- https://www.idealista.com/data/
- https://www.bankinter.com/blog/finanzas-personales/prevision-precio-vivienda





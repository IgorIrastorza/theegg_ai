# Tarea 22

## Enunciado
Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la Plaza del pueblo. 
Como es una persona muy prudente, desea que la leche que venderá sea perfectamente natural y fresca, y por esa razón, va a 
traer unas sanísimas vacas de desde Tolosa. Dispone de un camión con un cierto límite de peso, y un grupo de vacas disponibles 
para la venta. Cada vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día.
	
Se debe elegir qué vacas comprar y llevar en el camión, de modo que se pueda maximizar la producción de leche, observando el límite 
de peso del camión.
	
1. Para este propósito se tiene que definir las siguientes entradas:
   - *Entrada:* Número total de vacas en la zona de Tolosa que están a la venta.
   - *Entrada:* Peso total que el camión puede llevar.
   - *Entrada:* Lista de pesos de las vacas.
   - *Entrada:* Lista de la producción de leche por vaca, en litros por día.
	
2. El algoritmo que se programe tiene que calcular la siguiente salida:
   - *Salida:* Cantidad máxima de producción de leche se puede obtener.
___

## Solución
Este tipo de problemas recursivos requieren normalmente la comprobación de todas las soluciones posibles, obteniendo una relación 
exponencial en el aumento de operaciones a realizar a medida que el número de vacas crece. No obstante, con el objetivo de reducir 
el número de operaciones necesarias, este problema de optimización será resuelto mediante **programación dinámica**, que permite 
limitar el aumento del número de operaciones a una relación lineal.
	
La programación dinámica trata de resolver un problema complejo dividiendo este en subproblemas, más pequeños, resolviendo estos últimos
y combinar las soluciones obtenidas para calcular la solución del problema inicial. Este tipo de programación se emplea para resolver 
problemas de optimización que satisfacen el principio de optimalidad: en una secuencia óptima de decisiones toda subsecuencia ha de ser 
también óptima. En resumen: no calcular dos veces lo mismo y utilizar normalmente una tabla de resultados que se va rellenando a medida 
que se resuelven los subejemplares.
	
A continuación se desarrollará un pequeño ejemplo que facilite la comprensión de este metodo (será un ejemplo simplificado y al margen 
del enunciado de este problema para no alargarlo en exceso):

- ENUNCIADO: Maximiza el valor de los artículos que se introduciran en la bolsa teniendo en cuenta que sus asas no soportarán más de 
6 kilos de peso. Los objetos a considerar son los siguientes:
  - A: (3kg, 6€)
  - B: (5kg, 7€)
  - C: (6kg, 8€)
- SOLUCIÓN:
https://thales.cica.es/rd/Recursos/rd99/ed99-0033-04/din_introd.html

  - Etapa: Se puede definir como cada uno de los pasos que se deben seguir para llegar al objetivo. En este caso, cada objeto será una 
  etapa: 0, A, B, C
  - Estado: Son las diversas condiciones posibles en la que el sistema podría estar en esa etapa del problema. En este caso, los estados 
  serán el posible peso a introducir en la mochila: 0, 1, 2, 3, 4, 5, 6
  
  ![Ejemplo gráfico de etapas y estados](https://www.monografias.com/trabajos104/la-programacion-dinamica/image001.jpg)
  
  Una vez definido las distintas etapas y estados, es hora de aplicar el algoritmo mediante la ayuda de la siguiente tabla:

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| -- | -- | -- | -- | -- | -- | -- | -- |
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **A** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **B** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **C** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

  Como se observa, las referencias de las etapas se encuentran en la primera columna y las de los estados en la primera fila, aunque en el codigo del ejercicio se han omitido esa fila y columna. En el resto de casillas de la tabla se aplicará el siguiente algoritmo:
  
  ![Algoritmo a aplicar en cada etapa](C:/Users/igori/Documents/MEGA/Antolakuntza/The Egg/Github/theegg_ai/tarea_22/Algoritmo programación dinámica.png)
  
  O en código:
  ```python
for etapa in range (cantidadvacas+1):
    for estado in range (masacamion+1):
        if masavaca1[etapa]<=capacidadcamion[estado]:
            resta=capacidadcamion[estado]-masavaca1[etapa]
            matrix[etapa][estado]=prodvaca1[etapa]+matrix[etapa-1][resta]
        
        if matrix[etapa][estado]<matrix[etapa-1][estado]:
            matrix[etapa][estado]=matrix[etapa-1][estado]
```
 
 Este algoritmo permite que en cada etapa se consiga el mejor resultado de esa etapa y las anteriores, obteniendo el resultado óptimo al problema entero en la ultima etapa y estado. Por lo tanto, en el ejemplo que se ha planteado, el valor máximo (en €) que se podría introducir sería 8 y la tabla o matriz quedaría tal que así: 

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| -- | -- | -- | -- | -- | -- | -- | -- |
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **A** | 0 | 0 | 0 | 6 | 6 | 6 | 6 |
| **B** | 0 | 0 | 0 | 6 | 6 | 7 | 7 |
| **C** | 0 | 0 | 0 | 6 | 6 | 7 | 8 |



                

___

## Bibliografía
Más información sobre programación dinámica: 
- https://ocw.ehu.eus/pluginfile.php/9412/mod_resource/content/1/05_Programacion_Dinamica/05_Programacion_Dinamica.pdf
- https://www.youtube.com/watch?v=fVrPwSkSo0I&t=1736s
- https://www.ingenieria.unam.mx/sistemas/PDF/Avisos/Seminarios/SeminarioV/Sesion6_IdaliaFlores_20abr15.pdf
	

Más información sobre Notación O-Grande: 
- https://runestone.academy/runestone/static/pythoned/AlgorithmAnalysis/NotacionOGrande.html

Tarea 21

	ENUNCIADO
	Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la Plaza del pueblo. 
	Como es una persona muy prudente, desea que la leche que venderá sea perfectamente natural y fresca, y por esa razón, va a 
	traer unas sanísimas vacas de desde Tolosa. Dispone de un camión con un cierto límite de peso, y un grupo de vacas disponibles 
	para la venta. Cada vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día.
	
	Se debe elegir qué vacas comprar y llevar en su camión, de modo que se pueda maximizar la producción de leche, observando el límite 
	de peso del camión.
	
	1.- Para este propósito se tiene que definir las siguientes entradas:
	Entrada: Número total de vacas en la zona de Tolosa que están a la venta.
	Entrada: Peso total que el camión puede llevar.Entrada: Lista de pesos de las vacas.
	Entrada: Lista de la producción de leche por vaca, en litros por día.
	
	2.- El algoritmo que se programe tiene que calcular la siguiente salida:
	Salida: Cantidad máxima de producción de leche se puede obtener.

	SOLUCIÓN
	Este tipo de problemas recursivos requieren normalmente la comprobación de todas las soluciones posibles, obteniendo una relación 
	exponencial del numero de operaciones a realizar a medida que el número de vacas crece. No obstante, con el objetivo de reducir 
	el número de operaciones necesarias, este problema de optimización será resuelto mediante *programación dinámica*, que permite 
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
			- (3kg, 6€)
			- (5kg, 7€)
			- (6kg, 8€)
		- SOLUCIÓN:
			| |0|1|2|3|4|5|6|
			|--|--|--|--|--|--|--|--|
			|0|0|0|0|0|0|0|0|
			|--|--|--|--|--|--|--|--|
			|A|0|0|0|6|6|6|6|
			
			
	
	
	------------------------------------------
	Más información sobre programación dinámica: 
		- https://ocw.ehu.eus/pluginfile.php/9412/mod_resource/content/1/05_Programacion_Dinamica/05_Programacion_Dinamica.pdf
		- https://www.youtube.com/watch?v=fVrPwSkSo0I&t=1736s
		- https://www.ingenieria.unam.mx/sistemas/PDF/Avisos/Seminarios/SeminarioV/Sesion6_IdaliaFlores_20abr15.pdf
	
	Más información sobre Notación O-Grande: https://runestone.academy/runestone/static/pythoned/AlgorithmAnalysis/NotacionOGrande.html

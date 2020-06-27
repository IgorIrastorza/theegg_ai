Tarea 21

	ENUNCIADO
	Crea un programa que dado un número entre 0,0001 y 0,9999 (y de no más de 4 cifras decimales), obtenga y muestre la correspondiente fracción irreducible. 
	Por ejemplo, el número 0,25 se puede obtener a partir de 25/100, o de 2/8, o de 1/4, entre otros. La fracción irreducible es 1/4, que está formada por un numerador y un denominador que son primos entre sí.

	SOLUCIÓN
	Lo primero que se ha hecho es pasar el número introducido por el usuario a una fracción con denominador igual a 10000.
	La solución del problema ha venido mediante la aplicación del algoritmo de Euclides:
		- A será el denominador y B el numerador
		- Se escribe A en la forma cociente y residuo: A=B.Q+R
		- Se aplica la siguiente ecuación: MCD(A,B)=MCD(B,R), A=B y B=R
	
	El algoritmo se sigue aplicando hasta que A o B sean iguales a 0:
		- Si A=0, entonces MCD(A,B)=B
		- Si B=0, entonces MCD(A,B)=A
	
	Por último, se divide el denominador y el numerador por el MCD y se consigue la fracción irreducible.
	
	
	------------------------------------------
	Más información sobre el algoritmo Euclides: #https://es.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

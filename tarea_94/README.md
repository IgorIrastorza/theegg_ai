# Tarea 94

## Enunciado
Debes crear el siguiente módulo: se denominará `calculadora.py` y contendrá 4 funciones para realizar una suma, una resta, un producto y una división entres dos números. Todas las funciones devolverán el resultado.

Se deben tratar los siguientes errores:

1. En caso de que se envíen valores a las funciones que no sean números debe dar un aviso de tipo de error.

2. En caso de realizar una división por cero debe dar un aviso de tipo de error.

Una vez creado el módulo, crea un script `calculos.py` en el mismo directorio en el que deberás importar el módulo. Llama a todas las funciones del módulo y observa si el comportamiento es el esperado.

## Resolución

El primer paso al desarrollar la tarea ha sido definir las distintas funciones que tendrá el módulo de `calculadora.py`:
- `number()`: comprueba si los dos parametros de entrada (introducidos por el usuario) son en realidad números enteros. Si la comprobación es afirmativa, devuelve un `True`. Al contrario, si alguno de los parametros de entrada no es un número, devuelve un `False` y un error que aparece en pantalla.
- `addition()`: primero llama a la función `number()` para comprobar si los dos parametros son números. Si es así, devuelve la suma de los dos números. Si no devuelve un `NULL`.
-`susbtraction()`: primero llama a la función `number()` para comprobar si los dos parametros son números. Si es así, devuelve la resta del primer número menos el segundo número. Si no devuelve un `NULL`.
- `multiplication()`: primero llama a la función `number()` para comprobar si los dos parametros son números. Si es así, devuelve la multiplicación de los dos números. Si no devuelve un `NULL`.
- `division()`: primero llama a la función `number()` para comprobar si los dos parametros son números. Si es así, devuelve la división del primer número por el segundo número. Si no devuelve un `NULL`.

Por otro lado, se ha desarrollado un segundo programa (`calculos.py`) donde se pide al usuario que introduzca los dos números y se hacen las llamadas al módulo `calculadora.py` en función de la acción que desea realizar el usuario (suma, resta, multiplicación o división).

Ejemplo de ejecución:

`Introduce el primer número: 8`

`Introduce el segundo número: 45`

`-----------------------------------------------------------------`

`1. Sumar / 2. Restar / 3. Multiplicar / 4. Dividir`

`¿Qué desea realizar? Introduzca el número de la acción: 4`

`-----------------------------------------------------------------`

`Resultado de la división:  0.17777777777777778`




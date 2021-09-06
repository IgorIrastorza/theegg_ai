# Tarea 49

## Enunciado
Intenta comprender que significa la Programación Orientada a Objetos (POO) y define los siguientes conceptos: clase, objeto, método, propiedad/atributo, instancia, constructor, instancia, encapsulamiento, herencia. Debes profundizar y comprender qué significa esta nueva metodología para la programación y recapacitar en cómo afecta en tu manera de pensar a la hora de programar.

Posteriormente debes realizar estos ejercicios:
1. Crear una clase llamada `Persona`. Sus atributos son: `nombre`, `edad` y `DNI`. Construye los siguientes métodos para la clase:
   - Un constructor, donde los datos pueden estar vacíos.
   - Los setters y getters (métodos set y get) para cada uno de los atributos. Hay que validar las entradas de datos.
   - `mostrar()`: muestra los datos de la persona.
   - `esMayorDeEdad()`: devuelve un valor lógico indicando si es mayor de edad.

2. Crea una clase llamada `Cuenta` que tendrá los siguientes atributos: 
   - `titular` (que es una persona)
   - `cantidad` (puede tener decimales).

    El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
   - Un constructor, donde los datos pueden estar vacíos.
   - Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
   - `mostrar()`: muestra los datos de la cuenta.
   - `ingresar(cantidad)`: se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
   - `retirar(cantidad)`: se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

## Definición de los conceptos
La comprensión de la Programación Orientada a Objetos (POO) y sus principales conceptos están desarrollados y definidos en el diccionario general disponible en el repositorio `theegg_ai`.

## Ejercicio 1

En el primer archivo `Tarea 49_1.py` se encuentra el código para la construcción de la clase `Persona` y sus respectivos atributos y métodos. Tal y como pide el ejercicio, se han usado los decoradores `@property` y `@property.setter` para implementar los setters y getters.

- **Getter**: Se encargará de interceptar la lectura del atributo. (get = obtener)

- **Setter**: Se encarga de interceptar cuando se escriba. (set = definir o escribir)

Es por ello que cada vez que queramos leer el valor de un atributo el programa deberá llamar al método con el decorador `@property`. Siguiendo la misma lógica, cuando queramos cambiar el valor de un atributo privado el programa también llamará a la función setter con el decorador `@property.setter` para validar y asegurar el nuevo valor que se quiera escribir en el atributo.

Los tres atributos contienen algoritmos de validación dentro del getter para asegurarse de que cumplen con el formato requerido para el tipo de dato.

El programa también contiene una función `main()` para ejecutar un pequeño ejemplo de como funciona la clase construida.

Ejemplo de ejecución:

`Introduce tu nombre: Igor`

`Introduce tu DNI: 44875H`

`Formato de DNI incorrecto.`

`Introduce tu edad: 21`

`----------------------------------------------------------`

`Es mayor de edad: True`

`----------------------------------------------------------`

`- Nombre: Igor`

`- Edad: 21`

`- DNI: None`
'

### Ejercicio 2
En el segundo archivo `Tarea 49_2.py` se encuentra el script para la construcción de la clase `Cuenta` y sus respectivos atributos y métodos. El planteamiento del ejercicio es muy similar al anterior explicado arriba.

Al igual que en el anterior ejercicio, los atributos contienen algoritmos de validación dentro de los metodos getter y el programa también contiene una función `main()` para ejecutar un pequeño ejemplo de como funciona la clase construida.

Ejemplo de ejecución:


`Introduce tu nombre: Ig2r`

`Formato de nombre incorrecto.`

`Introduce la cantidad a ingresar: 500.25`

`Introduce la cantidad a retirar: 300.18`

`----------------------------------------------------------`

`- Titular de la cuenta: None`

`- Saldo total: 200.07`




## Bibliografía
- https://www.geeksforgeeks.org/getter-and-setter-in-python/
- https://platzi.com/tutoriales/1775-poo-python/5308-getters-y-setters-en-python/
- https://www.freecodecamp.org/news/python-property-decorator/#:~:text=The%20%40property%20is%20a%20built,of%20the%20use%20of%20%40property!





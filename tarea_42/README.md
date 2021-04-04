# Tarea 42

## Enunciado
El alumno para superar esta tarea debe:
1. Diseñar una estructura básica de HTML y verla en el navegador.
2. Introducir algo de color a la página apoyándose en CSS.
3. Añádir un video gracias a la nueva etiqueta video de html5.
4. Serías capaz de darle al play y al pause del video mediante instrucciones por voz (hablando a la computadora) utilizando javascript? (no obligatorio).

## Ejecución
Se ha diseñado una página web mediante la integración de tres archivos distintos:

- `index.html`: se ha definido la estructura de la página web y su contenido (menu/navegación principal, logo, busqueda, dos textos y dos videos, pie de página...). En este archivo se ha establecido el link con los otros archivos CSS y JavaScript.
- `style.css`: para darle el formato y diseño de la página web.
- `main.js`: para establecer los comandos por voz y activar el API de `annyang`.

## Ejecución
Para ejecutar y visualizar correctamente todas las funciones y complementos de la página web diseñada, es necesario crear un servidor virtual local en la ubicación donde se alojan los archivos web.

Para ello, recomiendo usar el módulo `SimpleHTTPServer` de Python. Los pasos a seguir para activarlo son muy sencillos:

1. **Instalar Python (si ya lo tienes salta al paso 2):** Ve a [python.org](https://www.python.org/downloads/) o instala directamente el paquete de [Anaconda](https://www.anaconda.com/products/individual).
2. **Abrir el CMD:** si tienes instalado Python mediante Anaconda, abre directamente el CMD de Anaconda `Anaconda Prompt`.
3. **Ir al directorio de los archivos web:** usamos el comando `cd` para llegar en este caso hasta la carpeta `tarea_42`.
4. **Activar el servidor local:** ejecutamos el comando `python -m http.server` en el CMD. Nos indicará en el puerto en el que se ha activado el servidor. Por defecto será en el puerto 8000 (METER FOTO):

![CMD](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_42/images/screenshot_1.png)

5. **Abrir `Google Chrome` (obligatorio para el correcto funcionamiento de los comandos por voz) y introducir la url `localhost:8000`** (METER FOTO):

![URL del navegador](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_42/images/screenshot_2.png)

Si no ha ocurrido ningún error, debería visualizar la siguiente página web (METER FOTO):

![Captura de pantalla de la página web](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_42/images/screenshot_3.png)

Para comprobar que el reconocimiento por voz están funcionando correctamente, puede utilizar el comando `Hola`, que devolverá una alerta de navegador. Si no funciona, comprueba que está entrando al archivo html mediante una petición `http`
 y que el navegador es `Google Chrome`.

## Comandos por voz
Los comandos por voz han sido creados gracias a la API de código abierto [annyang](https://www.talater.com/annyang/). Los comandos creados y sus respectivas funciones son las siguientes:

- `Hola`: devolverá una alerta de navegador saludando al usuario. Útil para probar si los comandos por voz están funcionando en el navegador.
- `Reproducir uno`: para reproducir el video de la izquierda.
- `Pausar uno`: para pausar el video de la izquierda.
- `Reproducir dos`: para reproducir el video de la derecha.
- `Pausar dos`: para pausar el video de la derecha.

## Bibliografía
- https://www.apachefriends.org/index.html
- https://www.talater.com/annyang/
- https://github.com/TalAter/annyang/blob/master/docs/README.md
- https://developer.mozilla.org/es/docs/Learn/Common_questions/set_up_a_local_testing_server
- https://www.faztweb.com/
    - https://www.youtube.com/watch?v=Q2imkhmhOFo&t=3726s
    - https://www.youtube.com/watch?v=rbuYtrNUxg4
- https://fontawesome.com
- https://www.freepik.com/photos/car
- https://fonts.google.com/





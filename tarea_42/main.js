var video1 = document.getElementById("video1");
var video2 = document.getElementById("video2");

//Aparecerá una alerta en el navegador si no funciona el reconocimiento por voz.//
if (!annyang) {
  alert("Tu navegador no soporta el reconocimiento de voz. Esto puede ser debido a dos razones: \n - No estas entrando en la aplicación mediante una solicitud http (no has creado el servidor local virtual). Lee atentamente los pasos a seguir leyendo el archivo README.md del repositorio. \n - El navegador con el que estas ejecutando la página web no es Google Chrome.");
};

//En este fragmento se han definido los comandos y el inicio de funcionamiento del paquete annyang.//
if (annyang) {
  var commands = {
    'Hola': function() {
      alert("Hola! Bienvenido a la tarea 42 de The Egg.ai");
    },
    'Reproducir uno': function(){
      video1.play();
    },
    'Pausar uno': function(){
      video1.pause();
    },
    'Reproducir dos': function(){
      video2.play();
    },
    'Pausar dos': function(){
      video2.pause();
    }
  };
  annyang.addCommands(commands);
  annyang.setLanguage("es-ES");
  annyang.start();
}
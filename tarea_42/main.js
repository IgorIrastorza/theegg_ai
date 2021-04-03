var video1 = document.getElementById("video1");
var video2 = document.getElementById("video2");

if (!annyang) {
  alert("Tu navegador no soporta el reconocimiento de voz. Esto puede ser debido a dos razones: \n - No estas entrando en la aplicación mediante una solicitud http. \n - El navegador con el que estas ejecutando la página web no es Chrome.");
};

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
# Tarea 39

## Enunciado
En esta tarea se simularán, mediante el simulador Cisco Packet Tracer, 5 redes distintas.
___

## Red 1: servidor web y DNS
El modelo estará compuesto por los siguientes elementos que estan integrados en una misma red 
con dirección IP 171.16.1.0 y mascára de subred 255.255.255.0:
- PC0
    - Dirección IP: 172.16.1.3
    - Máscara de subred: 255.255.255.0
    - Servidor DNS: 172.16.1.100
- PC1
    - Dirección IP: 172.16.1.4
    - Máscara de subred: 255.255.255.0
    - Servidor DNS: 172.16.1.100
- Servidor Web
    - Dirección IP: 172.16.1.1
    - Máscara de subred: 255.255.255.0
- Servidor DNS
    - Dirección IP: 172.16.1.100
    - Máscara de subred: 255.255.255.0

![Configuración de red](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS.png)

En el servidor web se han guardado los archivos html que contiene la página web, y en el servidor DNS, el nombre de la página y su correspondiente dirección IP. Cuando uno de los ordenadores tecleé una dirección en su navegador, este realizará primero una consulta DNS para saber en que dirección se encuentra el servidor web que aloja la pagina web. Una vez resuelta la consulta, el ordenador cliente establecerá comunicación con la dirección IP del servidor.

En este caso, para comprobar el correcto funcionamiento de la red, se ha navegado desde los PC a la pagina web "www.holamundo.es" previamente registrada en los servidores, obteniendo los siguientes resultados:

![Resultados de la navegación](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20web%20y%20DNS_comprobacion.png)

## Red 2: servidor DHCP

En este segundo ejercicio se ha construido una red en la que las direcciones IP se asignan dinámica y automaticamente gracias a un servidor DHCP. La configuración de red es la siguiente:

![Configuración de red](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20DHCP.png)

EL servidor DHCP se ha configurado de la siguiente manera:
- Dirección IP del servidor: 172.16.1.254
- Máscara de subred del servidor: 255.255.255.0

En cuanto al servicio DHCP que prestará:
- Puerta de enlace predeterminada: 172.16.1.1
- Servidor DNS: 172.16.1.100
- Asignación de direcciones IP a partir de: 172.16.1.2
- Máscara de subred: 255.255.255.0
- Número máximo de usuarios: 100

Para comprobar que el servicio DHCP ha funcionado correctamente en la configuración construida, se ha simulado el envio de mensajes entre los ordenadores conectados a la red:

![Comprobación de red](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Servidor%20DHCP_comprobacion.png)

## Red 3: VLAN básica

En el siguiente ejercicio se ha construido una red con distintas VLAN. Este tipo de redes, aunque fisicamente esten conectados a un mismo router o switch, permite crear redes virtuales diferentes e independientes, segmentando a los clientes y restrigiendo el acceso desde una red a otra. En la red diseñada se han usado dos VLAN distintas para los departamentos de recursos humanos (2) y sistemas (3), donde sus "clientes" se conectan a traves de dos switches que estan interconectados gracias a un enlace "trunk" en el último interfaz de cada switch. El enlace "trunk" se configura en uno o más puertos de un switch para permitir el paso del tráfico de las distintas VLANs que hemos creado.

Por lo tanto, el esquema de la red diseñada y los datos introducidos en cada elemento para su correcto funcionamiento son los siguientes:

![Configuración de red](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/VLAN%20b%C3%A1sica.png)

A continuación, se han llevado a cabo dos comprobaciones para comprobar que la red funciona correctamente:
- Comando "sh vlan" en los dos switches para comprobar las VLAN registradas y sus correspondientes interfaces.

![Comprobación de red 1](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/VLAN%20b%C3%A1sica_comprobaci%C3%B3n.png)

- Simulación de mensajes entre ordenadores clientes de la misma VLAN y distinta. Como se puede observar en los resultados obtenidos
solo ha sido satisfactorio el envio de mensajes entre los ordenadores pertenecientes a la misma VLAN.

![Comprobación de red 2](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/VLAN%20b%C3%A1sica_comprobaci%C3%B3n%201.png)

## Red 4: VLAN mediante router
En este ejercicio se crean tres redes VLAN en un switch, que posteriormente se comunican mediante un router. Esta topologia permitirá que diferentes VLAN se comuniquen entre si, ya que una estación que pertenece a una VLAN no puede comunicarse con ningún dispositivo de otra VLAN solo mediante un switch (Red 3) pero si mediante un router.

En este ejercicio se han creado las siguientes VLAN:

- VLAN SISTEMAS (2): puertos 1-8
- VLAN DESAROLLO (3): puertos 9-16
- VLAN REDES (4): puertos 17-23

Una vez conectados los clientes a su correspondiente interfaz del switch, esta se conecta al router mediante un enlace trunk (puerto 24). Una vez en el router, se usa el tipo de configuración “Router-on-a-stick” en la cual una única interfaz física enruta el tráfico entre varias VLAN en una red. Para ello, se crean tres distintas subinterfaces, que son interfaces virtuales basadas en software, asociadas con una única interfaz física; se configuran en software en un router, y cada subinterfaz se configura de manera independiente con una dirección IP y una asignación de VLAN.

En conclusión, la topología y los ajustes parametrizados en cada dispositivo son los siguientes:
![Configuración de red](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/VLAN%20mediante%20router.png)

Y las comprobaciones de que hay conexión entre mismas y distintas VLAN:
![Comprobación de red](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/VLAN%20mediante%20router_comprobaci%C3%B3n.png)

## Red 5: Enrutamiento estático
En este último ejercicio se ha construido una pequeña red MAN (Metropolitan Area Network) en la que tres LAN distintas se conectarán entre sí. Para ello, cada red tendrá su correspondiente router, que luego será conectado a la red MAN mediante una interfaz serial. La topologia de red y las parametros introducidos en cada elemento son los siguientes:

![Configuración de red](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Enrutamiento%20est%C3%A1tico.png)

Para que un paquete de datos pueda "viajar" desde una red a otra, se ha configurado en cada router una tabla de enrutamiento estático, donde se especifican dos direcciones de red: la primera para la red de destino final y la segunda para el siguiente destino de los datos. Por ejemplo, si en nuestra red el PCO quiere mandar un mensaje al PC4 (red: 10.1.50.0), en las tablas de enrutamiento del "Router0" y Router1" tendrán que aparecer los siguientes datos:
- Router0: 10.1.50.0/24 via 200.33.146.2
- Router1: 10.1.50.0/24 via 200.33.147.2

Así, la información irá primero al "Router0", donde gracias a la información de ruteo se redirigirá al "Router1" y "Router2", donde finalmente llegará a su destino.

![Comprobación de red](https://github.com/IgorIrastorza/theegg_ai/blob/master/tarea_39/images/Enrutamiento%20est%C3%A1tico_comprobaci%C3%B3n.png)

## Bibliografía
- https://www.itesa.edu.mx/netacad/introduccion/course/module8/8.1.2.3/8.1.2.3.html
- https://docs.microsoft.com/es-es/troubleshoot/windows-client/networking/tcpip-addressing-and-subnetting
- https://www.quia.com/files/quia/users/istomar/DIPS/mscara_de_subred.html
- http://itroque.edu.mx/cisco/cisco1/course/module3/3.3.3.1/3.3.3.1.html
- http://formacion.intef.es/pluginfile.php/37388/mod_resource/content/1/PDF_conlogonuevo/2-Servidor-DHCP-y-DNS.pdf
- https://www.redeszone.net/2016/11/29/vlans-que-son-tipos-y-para-que-sirven/
- https://www.redeszone.net/tutoriales/redes-cable/configurar-enlace-troncal-switch/
- https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/14976-50.html
- https://www.tecnologia-informatica.es/calcular-subredes/
- https://ccnadesdecero.es/routing-entre-vlan-router-on-a-stick/


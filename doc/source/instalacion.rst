===========
Instalación
===========


GNU/Linux
=========

El proceso de instalación en GNU tiene dos pasos, primero
debe asegurarse de tener todas las dependencias de software y
luego instalar quickdiagrams.


Dependencias
____________


Si cuenta con un sistema de paquetes basado en **apt**, como en los
sistemas Ubuntu GNU/Linux o Debian GNU/Linux, puede utilizar
el siguiente comando para instalar todo lo necesario::

    sudo apt-get install python-yapgvb

opcionalmente, si quiere ejecutar el programa en su equipo
sirviendo el servicio a traves de la red instale::

    sudo apt-get install python-webpy


Instalar quickdiagram
_____________________

La última versión estable del programa se encuentra en la siguiente
dirección:

http://code.google.com/p/quickdiagrams/

Acceda la sección de descargas y obtenga el archivo con extensión .tar.gz.

Luego, para instalar el programa ejecute::

    tar xzf quickdiagrams.tar.gz
    cd quickdiagrams
    sudo python setup.py install

Ya está, ahora tiene un nuevo comando dentro de su sistema 
llamado *quickclassdiagram*.


Windows
=======


Primero necesita instalar python, graphviz para windows y la biblioteca
yapgvb. Visite las siguientes páginas e instale las versiones .exe
de cada paquete:

    * http://www.python.org/
    * http://www.graphviz.org
    * http://code.google.com/p/yapgvb/

.. Si quiere utilizar el cliente gráfico también necesitará instalar
   la biblioteca GTK y su extensión para python:


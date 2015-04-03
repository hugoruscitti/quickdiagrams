# About #

**quickDiagrams** permite crear diagramas de clase a partir de un archivo
de texto muy sencillo.

Este proyecto utiliza graphviz y la biblioteca [python-yapgvb](http://code.google.com/p/yapgvb).


### Resultado de ejemplo ###

El siguiente grafico:

![http://quickdiagrams.googlecode.com/files/foro_de_mensajes.png](http://quickdiagrams.googlecode.com/files/foro_de_mensajes.png)

es resultado creado a partir del siguiente archivo de texto:

```
Usuario
    nick
    nombreCompleto
    email
    permisos

    recordarContraseña()

Foro
    nombre

    ForoPrivado
        permisosDeAcceso

Mensaje
    titulo


1 Usuario * mensajes
1 foro tiene muchos mensajes
```



# Interfaz de linea de comandos #

Este programa se utiliza principalmente desde
un interprete de comandos como bash:


```
Usage: quickclassdiagram [options]

Options:
  -h, --help            show this help message and exit
  -i FILE, --input=FILE
                        file input
  -o FILE, --output=FILE
                        file output
  -d DEBUG, --debug=DEBUG
                        sets debug mode
  -f FORMAT, --format=FORMAT
                        example: png, svg ...
```

**Ejemplo de uso**

Este programa generará una imagen llamada **output\_model.png**.

```
quickclassdiagram -i model.sc -o output_model.png
```


# Interfaz Web #

Puede probar este programa directamente desde
su navegador ingresando en:

  * http://www.diagramadeclases.com.ar

En el repositorio encontrará la aplicación python
que le permitirá tener su propio sitio web con
quickdiagrams.

# Interfaz de escritorio #

También contamos con una versión de escritorio del
programa.

Aquí solamente tiene que escribir el modelo en la
parte izquierda de la ventana y observar el resultado
a la derecha.

### Quickdiagrams sobre GNU/Linux ###
![http://quickdiagrams.googlecode.com/files/gtk.png](http://quickdiagrams.googlecode.com/files/gtk.png)


## Quickdiagrams sobre Windows ##
![http://quickdiagrams.googlecode.com/files/windows.png](http://quickdiagrams.googlecode.com/files/windows.png)


# Videos #


<a href='http://www.youtube.com/watch?feature=player_embedded&v=zTMwOJopTus' target='_blank'><img src='http://img.youtube.com/vi/zTMwOJopTus/0.jpg' width='425' height=344 /></a>
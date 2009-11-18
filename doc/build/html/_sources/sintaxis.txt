Sintaxis
========

Para definir lo diagramas tienes que escribir la definición
de las clases una por una, la primer linea de la clase debe
ser el nombre, luego los atributos y por último los métodos.

Es importante que entre el nombre de la clase y los
atributos definas una separación o identación, por ejemplo::

    Persona
        nombre
        apellido
        ---
        saludar


Subclases
---------

Para representar subclases solo se debe identar a partir
de la clase padre. El nombre de la nueva clase tiene que
estar al mismo nivel que los atributos de la clase que implementa, por
ejemplo::

    Vehiculo
        kms

        Automóvil
            modelo
            ---
            avanzar()


Métodos implícitos
------------------

Cuando define un modelo generalmente se puede advertir y distinguir
cuando algo es un método o no, así que **quickdiagrams** trata
de ayudar en eso.

Por ejemplo, si un atributo incluye caracteres cómo ``(`` o ``:``, se
asumirá que el atributo es el nombre de un método, así que no
hace falta separar con guiones variables y métodos.

Veamos un ejemplo, la siguiente clase tiene dos atributos y dos métodos::

    Foro
        identificador
        publicar(mensaje)
        titulo
        inscribir_usuario(nombre)


Clases vacías
-------------

Si quiere crear clases sin especificar ninguno de sus atributos, algo
útil cuando quiere obtener un diagrama de diseño inicial, puede utilizar
el guión bajo como atributo 'transparente'::

    ClaseSinContenido
        _

    OtraClaseVacia
        _

        SubclaseVacia
            _

Otra utilidad de los guiones, es que puedas utilizarlos para agrupar
atributos de los objetos produciendo espacios. Una idea horrible, pero
que tal vez quieras utilizar::

    UnaClase
        atributo_1
        atributo_2
        _
        atributos_separados_1
        atributos_separados_2

        metodo()


Relaciones
==========

Introducción
------------

Para definir relaciones en un diagrama solamente tiene
que citar el nombre de las clases en una linea
sin sangrías.

Este ejemplo define una relación entre clases::

    Usuario Correo

.. image:: images/simple_relation.png


Si en cambio quiere lineas con dirección o señalando
agregación utilice paréntesis angulares::


    cuaderno <>- hoja
    libro -> cuaderno
    carpeta -> cuaderno

.. image:: images/relacion_compleja.png



Referencia
----------

Esta es una tabla de los tipos de relaciones mas utilizados:


+-----------------+-------------------------------------------+
| Referencia      | Imagen de ejemplo                         |
+=================+===========================================+
| ``A B``         | |simple|                                  |
+-----------------+-------------------------------------------+
| ``A - B``       | |simple|                                  |
+-----------------+-------------------------------------------+
| ``A -> B``      | |a_derecha|                               |
+-----------------+-------------------------------------------+
| ``A <- B``      | |a_izquierda|                             |
+-----------------+-------------------------------------------+
| ``A mensaje B`` | |mensaje|                                 |
+-----------------+-------------------------------------------+
| ``1 A * B``     | |cardinalidad|                            |
+-----------------+-------------------------------------------+
| ``A <>-> B``    | |a_derecha_diamante|                      |
+-----------------+-------------------------------------------+
| ``A <-<> B``    | |a_izquierda_diamante|                    |
+-----------------+-------------------------------------------+
| ``A <>- B``     | |a_derecha_diamante_simple|               |
+-----------------+-------------------------------------------+
| ``A -<> B``     | |a_izquierda_diamante_simple|             |
+-----------------+-------------------------------------------+
| ``A <*>- B``    | |a_derecha_diamante_simple_lleno|         |
+-----------------+-------------------------------------------+
| ``A -<*> B``    | |a_izquierda_diamante_simple_lleno|       |
+-----------------+-------------------------------------------+


.. |a_derecha| image:: images/relaciones/a_derecha.dot.png
.. |a_izquierda| image:: images/relaciones/a_izquierda.dot.png
.. |cardinalidad| image:: images/relaciones/cardinalidad.dot.png
.. |mensaje| image:: images/relaciones/mensaje.dot.png
.. |simple| image:: images/relaciones/simple.dot.png
.. |a_derecha_diamante| image:: images/relaciones/a_derecha_diamante.dot.png
.. |a_izquierda_diamante| image:: images/relaciones/a_izquierda_diamante.dot.png
.. |a_derecha_diamante_simple| image:: images/relaciones/a_derecha_diamante_simple.dot.png
.. |a_izquierda_diamante_simple| image:: images/relaciones/a_izquierda_diamante_simple.dot.png
.. |a_derecha_diamante_simple_lleno| image:: images/relaciones/a_derecha_diamante_simple_lleno.dot.png
.. |a_izquierda_diamante_simple_lleno| image:: images/relaciones/a_izquierda_diamante_simple_lleno.dot.png

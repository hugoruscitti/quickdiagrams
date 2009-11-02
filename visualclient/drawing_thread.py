# -*- encoding: utf-8-
# Copyright: Hugo Ruscitti <hugoruscitti@gmail.com>
# License: GPLv3

import time
from threading import Thread
import gtk


class DrawingThread(Thread):
    """Representa el componente del programa que dibuja los diagramas.

    Este componente actua de manera desacoplada por medio de un hilo, para
    no interferir en la interfaz de usuario gtk."""

    def __init__(self, main, queue):
        Thread.__init__(self)
        self.queue = queue
        self.main = main

    def run(self):

        while True:
            # Espera sin gastar recursos hasta que llegue una
            # nueva tarea.

            task = None

            
            while not self.queue.empty():
                task = self.queue.get()        # agota la cola para quedarse 
                                               # con la ultima tarea.

            task = self.queue.get()        # agota la cola para quedarse 
            if task:
                task()
            else:
                return

            self.queue.task_done()

            # Descarta todas las tareas antiguas
            while not self.queue.empty():
                self.queue.get()
                self.queue.task_done()

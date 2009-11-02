# -*- encoding: utf-8-
# Copyright: Hugo Ruscitti <hugoruscitti@gmail.com>
# License: GPLv3

import gtk
import re
import sys
import gtk.glade
import quickdiagrams
import dialogs
import gtkcodebuffer
import drawing_thread
import Queue
import gobject


gobject.threads_init()

if sys.platform == "win32":
    TEMPORALY_FILEOUTPUT = "output.png"
else:
    TEMPORALY_FILEOUTPUT = "/tmp/output.png"


class View(object):
    pass


class Application:

    def __init__(self):
        self.ui = gtk.glade.XML('ui.glade')
        self._connect_callbacks(self.ui)
        self._create_view(self.ui)
        self._create_buffer()

        # TODO: se podria usar una cola lifo, pero python2.5 no lo tiene.
        self.queue = Queue.Queue()
        self.drawing_thread = drawing_thread.DrawingThread(self, self.queue)
        self.drawing_thread.start()

        self.buffer.connect("changed", self.custom_on_buffer__changed)
        background_color = gtk.gdk.color_parse("white")
        self.view.eventbox.modify_bg(gtk.STATE_NORMAL, background_color)
        self.request_draw_to_drawing_thread()
        self.last_lines_in_model = 0
        self.set_buffer_has_modified(False)
        self.document_name = ""

    def _create_buffer(self):
        emph  = gtkcodebuffer.String(r"\*", r"\*", style="datatype")
        emph2 = gtkcodebuffer.String(r"\*\*", r"\*\*", style="datatype")
        code  = gtkcodebuffer.String(r'`', r'`', style="special")
        head  = gtkcodebuffer.Pattern(r"^#+.+$", style="keyword")
        list1 = gtkcodebuffer.Pattern(r"^(- ).+$", style="comment", group=1)
        list2 = gtkcodebuffer.Pattern(r"^(\d+\. ).+$", style="comment", group=1)
         
        lang = gtkcodebuffer.LanguageDefinition([emph, emph2, code, head, list1, list2])

        self.buffer = gtkcodebuffer.CodeBuffer(lang=lang)
        self.view.textview.set_buffer(self.buffer)
        self.set_model_text("""Foro
    nombre
    mensajes
    ----
    publicar

    ForoPrivado
        permisos""")

    def request_draw_to_drawing_thread(self):
        self.queue.put(self.draw_diagram)

    def custom_on_buffer__changed(self, widget):
        # Detecta si se ha creado una nueva linea.
        text_model = self.get_model_text_as_list()
        lines = len(text_model)

        if lines != self.last_lines_in_model:
            self.last_lines_in_model = lines

        self.request_draw_to_drawing_thread()

        self.set_buffer_has_modified(True)

    def set_buffer_has_modified(self, state):
        self.has_modified = state
        title = "quickdiagrams"

        if state:
            title = title + " [sin guardar]"
        
        self.view.save.set_sensitive(state)
        self.view.window.set_title(title)

    def draw_diagram(self):
        self.diagram = quickdiagrams.Diagram()
        text_model = self.get_model_text_as_list()
        self.diagram.read_from_string(text_model)
        self.diagram.save(TEMPORALY_FILEOUTPUT, 'png', disable_output=True)
        self.update_image()

    def update_image(self):
        gobject.idle_add(self.update_image_callback)

    def update_image_callback(self):
        self.view.image.clear()
        self.view.image.set_from_file(TEMPORALY_FILEOUTPUT)

    def get_model_text_as_list(self):
        start, end = self.buffer.get_bounds()
        return self.buffer.get_text(start, end).split('\n')

    def set_model_text(self, text):
        self.buffer.set_text(text)

    def _connect_callbacks(self, ui):
        "Conecta automagicamente todos los eventos que parecen callbacks."

        expresion = re.compile("on_(.*)__(.*)")
        methods_list = [x for x in dir(self) if expresion.match(x)]

        for method in methods_list:
            result = expresion.search(method)
            widget_name = result.group(1)
            signal = result.group(2)

            widget = ui.get_widget(widget_name)
            function = getattr(self, method)
            widget.connect(signal, function)

    def _create_view(self, ui):
        "Extrae todas las referencias a widgets y las agrupa en 'view'."
        widgets_list = ui.get_widget_prefix("")
        self.view = View()

        for widget in widgets_list:
            name = widget.name
            setattr(self.view, name, widget)

    def save_to(self, filename):
        text_model_as_list = self.get_model_text_as_list()
        content = '\n'.join(text_model_as_list)
        file = open(filename, "wt")
        file.write(content)
        file.close()
        self.set_buffer_has_modified(False)

    def open_file(self, filename):
        file = open(filename, "rt")
        self.set_model_text(file.read())
        file.close()
        self.set_buffer_has_modified(False)

    def export_to(self, filename):
        self.diagram = quickdiagrams.Diagram()
        text_model = self.get_model_text_as_list()
        self.diagram.read_from_string(text_model)
        self.diagram.save(filename, 'png')


    # Callbacks
    def on_open__clicked(self, widget):
        pattern = ("ClassDiagram *.sc", "*.sc")
        dialog = dialogs.OpenDialog(self.view.window, pattern, self.open_file)
        dialog.run()

    def on_window__delete_event(self, widget, extra):
        "Intenta cerrar el programa pero consultando al usuario si no ha guardado."

        if not self.has_modified or self.show_confirm_dialog():
            gtk.main_quit()
            self.kill_child_thread()
        else:
            return True

    def kill_child_thread(self):
        self.queue.put(None)
        self.drawing_thread.join()

    def on_save__clicked(self, widget):
        pattern = ("ClassDiagram *.sc", "*.sc")
        dialog = dialogs.SaveDialog(self.view.window, pattern, self.save_to)
        dialog.run()

    def on_export__clicked(self, widget):
        pattern = ("PNG", "*.png")
        dialog = dialogs.SaveDialog(self.view.window, pattern, self.export_to)
        dialog.run()

    def on_about__clicked(self, widget):
        self.view.aboutdialog.run()
        self.view.aboutdialog.hide()

    def show_confirm_dialog(self):
        leave = self.view.leave
        response = leave.run()
        leave.hide()
        return response


def main():
    app = Application()
    app.view.window.show()
    gtk.main()


if __name__ == '__main__':
    main()
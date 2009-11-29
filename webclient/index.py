# -*- encoding: utf-8 -*-
import sys
import web
import uuid
import time
import os
import re
import xml.sax.saxutils

# para pruebas locales.
sys.path.insert(0, '../')
import quickdiagrams

URL = "http://www.diagramadeclases.com.ar"

urls = (
    '/', 'HomePage',
    '/draw', 'DrawCommand',
    '/save', 'SaveCommand',
    '/(\w{6})', 'DisplayCommand',
    )


this_dir = os.path.dirname(os.path.abspath(__file__))
render = web.template.render(os.path.join(this_dir, 'templates/'))
app = web.application(urls, globals())


class HomePage:

    def GET(self):

        code = """
Usuario
	nick
	email
	recordarContraseña()

Foro
	nombre

	ForoPrivado
		permisos

Mensaje
	titulo

1 Usuario * mensajes
1 foro tiene * mensajes
"""
        return render.index(code, web.ctx.homedomain)


class DrawCommand:
    """Dibuja el modelo indicado por medio de POST."""

    def POST(self):
        input = web.input()

        if not input.has_key('diagram_code'):
            return "Error: invalid post data"

        code = input['diagram_code']
        code = xml.sax.saxutils.unescape(code)
        diagram = quickdiagrams.main.Diagram()
        diagram.read_from_string(code.encode('utf8').split('\n'))

        # Genera el archivo de salida.
        t = time.time()
        file_output = "static/tmp/%d_%s.png" %(t, uuid.uuid4())
        full_path = os.path.join(this_dir, file_output)
        diagram.save(full_path, 'png', disable_output=True)


        #self.remove_old_files()

        return file_output

    def remove_old_files(self):
        "Elimina los archivos antiguos del servidor."

        this_dir = os.path.dirname(os.path.abspath(__file__))
        tmpdir = os.path.join(this_dir, "static", "tmp")
        t = int(time.time())
        files_to_remove = [os.path.join(tmpdir, name) for name in os.listdir(tmpdir) 
                if self.is_imagefile(name) and self.is_old_file(t, name)]

        map(os.remove, files_to_remove)

    def is_old_file(self, this_time, filename):
        "Informa si un archivo es muy antiguo en base a la marca de tiempo."

        # TODO: usar fecha de archivos en lugar de codificarlas en el nombre.
        try:
            file_time = int(filename.split('_')[0])
            dt = this_time - file_time
            return dt > 60 # elimina archivos que tienen mas de un minuto.
        except ValueError:
            pass

        return False

    def is_imagefile(self, filename):
        return filename.endswith(".png")


class SaveCommand(DrawCommand):

    def POST(self):
        input = web.input()
        code = input['diagram_code']
        code.encode('utf8')

        diagram_name = self.create_diagram_name()
        self.save_model(diagram_name, code.encode('utf8'))

        #url = "%s/%s" %(web.ctx.homedomain, diagram_name)
        url = "%s/%s" %(URL, diagram_name)
        link = "<a href='%s'>%s</a>" %(url, url)
        message = "Guardando los cambios en: <ul><li>%s</li></ul>" %link
        return message

    def create_diagram_name(self):
        return str(uuid.uuid4())[0:6]

    def save_model(self, diagram_name, code):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(this_dir, "static", "tmp", diagram_name + ".txt")

        file = open(filename, "wt")
        file.write(code)
        file.close()


class DisplayCommand(DrawCommand):
    """Muestra la pagina principal con un modelo recuperado."""

    def GET(self, diagram_name):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(this_dir, "static", "tmp", diagram_name + ".txt")

        try:
            file = open(filename, "rt")
            content = file.read()
            file.close()
        except IOError:
            return render.index("", web.ctx.homedomain, "Lo siento, no se puede recuperar el modelo solicitado (%s). " %(diagram_name))

        return render.index(content, web.ctx.homedomain)


if __name__ == '__main__':
    print "Starting web server at:\n\t",
    application = web.application(urls, globals())
    application.run()
else:
    application = web.application(urls, globals()).wsgifunc()

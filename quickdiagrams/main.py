# -*- coding: utf-8 -*-
import yapgvb
import parser
import pac_parser

class Diagram:
    """Representa un diagrama completo."""

    def __init__(self, disable_visible_warnings=False):
        self.content = []
        self.digraph = yapgvb.Digraph()
        self.nodes = {}
        self.digraph.rankdir = "BT"
        self.digraph.nodesep = 1
        self.disable_visible_warnings = disable_visible_warnings

    def add_warning_message(self, message):
        "Mustra un mensaje de advertencia en el diagrama."

        print "Cuidado: " + message

        if not self.disable_visible_warnings:
            node = self.digraph.add_node(message)
            node.shape = 'record'
            node.fontsize = 10
            node.fontname = "Verdana"
            node.color = "red3"
            node.fontcolor = "red3"
            node.label = "cuidado: \n" + message

    def read(self, input_file_name):
        "Lee un modelo de clases desde un archivo de texto."

        if self._is_pac_filename(input_file_name):
            file_handler = pac_parser.get_fakefile(input_file_name)
        else:
            file_handler = open(input_file_name, 'rt')

        filecontent = file_handler.readlines()
        self.read_from_string(filecontent)
        file_handler.close()

    def _is_pac_filename(self, input_file_name):
        "Informa si un nombre de archivo parece un archivo .pac"
        return input_file_name.lower().endswith(".pac")

    def read_from_string(self, filecontent):
        "Lee un modelo de clases desde una lista de cadenas."

        models, relationships = \
            parser.create_models_and_relationships_from_list(filecontent)

        # TODO: que la funcion reporte solamente la lista vacia en lugar de
        #       un solo valor como None.
        if models == [None]:
            self.add_empty_node()
        else:
            for model in models:
                self.add_model(model)

        self.create_hierarchy_relationships()
        self.create_explicit_relationships(relationships)

    def add_model(self, model):
        "Genera un nodo de clase para el modelo indicado."

        node = self.digraph.add_node(str(model.name))
        node.shape = 'record'
        node.fontsize = 10
        node.fontname = "Verdana"
        node.label = model.get_content_as_string()
        
        if model.name:
            name = model.name.lower()
        else:
            name = "??"

        self.nodes[name] = (model.superclass, node)

    def add_empty_node(self):
        "Genera un nodo indicando que el modelo está vacío."

        node = self.digraph.add_node("Empty model")
        node.shape = 'none'
        node.fontsize = 10
        node.fontname = "Verdana"
        #node.fontcolor = 'gray'

    def get_node_from_name(self, name):
        """Obtiene un nodo asociado a un determinado nombre de clase.

        Este método intenta reconocer clases por su nombre incluso si
        difieren en cantidad (ej. Auto ~= autos)."""

        # TODO: delegar en otro método e incluir casos como Pez ~= peces.
        # ver diveintopython
        name = name.lower()

        if not self.nodes.has_key(name):
            name_without_last_word = name[:-1]

            if self.nodes.has_key(name_without_last_word):
                return self.nodes[name_without_last_word][1]
        
        return self.nodes[name][1]

    def create_hierarchy_relationships(self):
        for key, value in self.nodes.items():
            superclass, node = value

            if superclass:
                superclass_node = self.get_node_from_name(superclass)
                edge = self.digraph.add_edge(node, superclass_node)
                edge.arrowhead = 'onormal'
                edge.arrowtail = 'none'

    def create_explicit_relationships(self, relationships):
        """Genera las relaciones que el usuario indica manualmente.

        Estas relaciones se definen en el modelo de datos
        utilizando una sintaxis como::
        
            1 Vehiculo tiene * Pasajeros
        """

        for rel in relationships:
            try:
                from_node = self.get_node_from_name(rel.from_name)
                to_node = self.get_node_from_name(rel.to_name)
            except KeyError, msg:
                msg_error = "No se encuentra la clase %s al crear una relación."
                self.add_warning_message(msg_error %(msg))
                return

            self.create_relation(from_node, to_node, rel)

    def create_relation(self, from_node, to_node, rel):
        edge = self.digraph.add_edge(from_node, to_node)
        edge.arrowtail = rel.arrowhead
        edge.label = rel.description
        edge.fontsize = 10
        edge.fontname = "Verdana"
        edge.taillabel = rel.from_counter
        edge.headlabel = rel.to_counter
        edge.arrowhead = rel.arrowtail

    def save(self, filename, format, disable_output=False):
        self.digraph.layout(yapgvb.engines.dot)
        self.digraph.render(filename, format)

        if not disable_output:
            print "Creating file: %s" %(filename)
        

if __name__ == '__main__':
    diagram = Diagram()
    diagram.read_from_string(['Process', '\tpid', '\tkill()'])
    diagram.save('test.png', 'png')
